########## import
import requests, json, time
from bybit.trade import *
from datetime import datetime
########## fonctions

###### Permet à partir du texte de récuperer le SL
def stopLoss(text): 
   tabNombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
   price = text[text.index("Stop :**")+8:]
   start = None
   end = None
   for i in range(len(price)):
      if price[i] in tabNombres:
         if start == None:
            start = i
         end = i
      elif end != None:
         break
   return price[start:end+1]

###### Permet à partir du texte de récuperer les TP
def takeProfit(text):
   tps = []
   tabNombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
   index = 0
   while(True):
      index +=1
      try :
         tpPrice = text[text.index("TP "+str(index)+" :**")+9:]
      except:
         break
      for i in range(len(tpPrice)):
         if tpPrice[i] not in tabNombres:
            tpPrice = tpPrice[:i]
            break
      tps.append(tpPrice)
   return tps


###### Permet à partir du texte de récuperer l'entrée
def enterPrice(text):
   tabNombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
   price = text[text.index("Entrée :**")+11:]
   for i in range(len(price)):
      if price[i] not in tabNombres:
         price = price[:i]
         break
   return price

def risk(text):
   tabNombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
   text = text[text.index("Stop :**")+11:]
   start = None
   end = None
   for i in range(len(text)):
      if text[i] == "-":
         if start == None:
            start = i+1
      elif start != None and text[i] in tabNombres:
         end = i
      elif end != None:
         break
   return text[start+1:end+1]
def boucle ():
   channelId = "990628352543047741" # ID du channel
   idLastMessage = None
   tradeSymbol = "---\n**__Nouveau trade potentiel__**" ### Symbol nouveau trade dans le message
   header = {
      "authorization": "##TOKEN DISCORD##"
      } ###Token du compte discord
   lancement = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
   compteur = 0
   duree = 60*60*12
   temps = time.time()
   writeDiscord("Lancement du programme le "+ lancement)
   while True:
      if time.time()-temps > duree:
         temps = time.time()
         writeDiscord("Programme toujours en route depuis le "+ lancement)
      try:
         r = requests.get("https://discord.com/api/v9/channels/"+channelId+"/messages", headers=header)
         if (r.status_code == 200):
            compteur = 0
            jsonn = json.loads(r.text)
            message = jsonn[0]
            if idLastMessage != message['id']: ### Si le message n'est pas le même que le dernier récupéré
               idLastMessage = message['id']
               text = message['content']
               if tradeSymbol in text[:len(tradeSymbol)]: ### Si le message contient le symbol de nouveau trade
                  trade = {}
                  ###### Récupération de toutes les informations
                  trade["Coin"] = text[text.index("**$")+3:text.index("\n**Id")]+"USDT"
                  trade["Price"] = enterPrice(text)
                  trade["Tps"] = takeProfit(text)
                  trade["Sl"] = stopLoss(text)
                  trade["Side"] = "Buy" if float(trade["Price"]) > float(trade["Sl"]) else "Sell"
                  trade["R"] = risk(text)
                  writeDiscord(launchTrade(trade))
         else :
            compteur += 1
            if compteur == 10:
               writeDiscord("Error requests channel discord")
      except Exception as e:
         writeDiscord("Big Error : "+ str(e))


def writeDiscord(message):
   playload = {
      'content': message
   }
   header = {
      "authorization": "Bot ##TOKEN##"
   }
   r = requests.post(URLDISCORD, data=playload, headers = header)
