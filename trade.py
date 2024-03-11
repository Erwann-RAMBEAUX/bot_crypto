from pybit.unified_trading  import HTTP
from .constant import *
from message.bot import *
import time

########## Fonctions

#### function principale appelée par bot.py
def launchTrade(trade):
    session = HTTP(     ###### Création de la connexion HTTP
        testnet = False,
        api_key = APIKEY,
        api_secret = APISECRET,
    )
    try :
        listTicker = get_ticker_list(session)
        ordre = session.get_positions(
            category = "linear",
            symbol = trade["Coin"],
        )
        if trade["Coin"] in listTicker and ordre["result"]["list"][0]["size"] == "0": # Vérification que le coin est dispo
            quantity = placeOrder(trade, session) # Placement du trade
            sizeTp = size_tp(quantity, trade, session)
            tp_place = place_tp(trade, sizeTp, session)
            message = "**__New Trade__**\n\n**Coin** : " + trade["Coin"] 
            message +="\n**Side** : " + trade["Side"] + "\n**Enter Price** : " + trade["Price"] + "\n"
            message += "**Quantity** : " + str(qty_trade(trade, session)) + "\n**Stop Loss** : " + trade["Sl"] + "\n"
            message += "**Take Profit** : \n"
            index = 0 
            for tp in trade["Tps"]:
                index += 1
                message += "**TP"+str(index)+"** : " + tp + "\n"
            if not tp_place :
                message += "```diff\n-Attention les TP ne sont pas placés !\n```"
        else : 
            message = "**__Trade not possible__**\n\n**Coin** : " + trade["Coin"] + "\n**Side** : " + trade["Side"] + "\n**Already in Position or Not Available**"
    except Exception as e:
        message = str(e)
    return message






#### Liste des tickers dispo sur bybit
def get_ticker_list(session):
    result = session.get_tickers(
            category="linear"
            ).get('result')['list']
    tickers = [asset['symbol'] for asset in result if asset['symbol'].endswith('USDT')]
    return tickers


#### Place un ordre
def placeOrder(trade,session):
    quantity = qty_trade(trade,session)
    session.place_order(
        category = "linear",
        symbol = trade["Coin"],
        #isLeverage = 1,
        side = trade["Side"],
        orderType = "limit",
        qty = quantity,
        price = trade["Price"],
        timeInForce = "GTC",
        stopLoss = trade["Sl"],
        takeProfit = trade["Tps"][-1],
        triggerPrice = trade["Price"],
        triggerDirection = 1 if current_price(trade["Coin"],session) < trade["Price"] else 2,
    )
    return quantity

#### Quantité d'un trade à partir du risk
def qty_trade(trade, session):
    enter = float(trade["Price"])
    sl = float(trade["Sl"])
    capital = get_capital_usdt(session)
    max_risk = RISK*float(trade["R"])*capital
    risk_coin = abs(enter-sl)
    qty = max_risk / risk_coin
    actual_price = current_price(trade["Coin"],session)
    if float(actual_price) < 10:
        qty = round(qty, 0)
    elif float(actual_price) < 100:
        qty = round(qty, 1)
    elif float(actual_price) < 10000:
        qty = round(qty, 2)
    else : 
        qty = round(qty, 3)
    return qty


#### Capital disponible pour trader en USDT
def get_capital_usdt(session):
    capital = session.get_wallet_balance(
        accountType = "UNIFIED",
        coin = "USDT"
    )
    return round(float(capital["result"]["list"][0]["coin"][0]["availableToWithdraw"]),1)


#### Prix actuel d'un coin
def current_price(coin, session):
    price = session.get_mark_price_kline(
        category = "linear",
        symbol = coin,
        interval = "1",
        limit = 1
    ).get('result').get('list', None)[0][4]
    return price


#### Connaitre la quantité de chaque TP en divisant la quantité du trade par le nombre de TP
def size_tp(quantity, trade, session):
    size = quantity / len(trade["Tps"])
    actual_price = current_price(trade["Coin"],session)
    if float(actual_price) < 10000:
        size = round(size, 2)
    elif float(actual_price) < 100:
        size = round(size, 1)
    elif float(actual_price) < 10:
        size = round(size, 0)
    else : 
        size = round(size, 3)
    return size
    

#### Placer tous les TP hormis le TP final
def place_tp(trade, size, session):
    duree = 60*2
    temps = time.time()
    while time.time()-temps < duree:
        ordre = session.get_positions(
            category = "linear",
            symbol = trade["Coin"],
        )
        if ordre["result"]["list"][0]["size"] != "0":
            break
        time.sleep(5)
    if (time.time() - temps < duree):
        for tp in trade["Tps"][:-1]:
            session.set_trading_stop(
                category = "linear",
                symbol = trade["Coin"],
                takeProfit = tp,
                tpTriggerBy = "MarkPrice",
                tpslMode="Partial",
                tpOrderType="Market",
                tpSize = str(size),
            )
        return True
    else :
        return False