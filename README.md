# Bybit Crypto Copy-Trading Bot

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Library](https://img.shields.io/badge/Library-pybit-orange.svg)
![Library](https://img.shields.io/badge/Library-discord.py-7289DA.svg)
![Status](https://img.shields.io/badge/Status-Inactive%20%2F%20Archived-red.svg)

This project was a Python script designed to automate copy-trading on the Bybit exchange. It was built to parse trading signals posted by the user "CryptoPicsou" on Discord and automatically execute corresponding trades. The script also included a companion Discord bot to announce all new trades it opened.

---

> ⚠️ **Project Archived: This Bot is No Longer Functional**
>
> This repository is maintained for informational and archival purposes only. The APIs, endpoints, and message-parsing logic are outdated and **will not work**. Do not attempt to use this script for live trading.

## Archived Features

* **Real-time Signal Monitoring:** Listened to a specific Discord channel for new messages from the target user ("CryptoPicsou").
* **Signal Parsing:** Analyzed message content to detect and extract trade opportunities (e.g., currency pair, entry price, stop-loss, take-profit).
* **Automated Trade Execution:** Used the `pybit` library to automatically place orders on Bybit based on the parsed signals.
* **Trade Notifications:** A separate Discord bot instantly announced any new trade opened by the script to a specified private channel.

## Technology Stack

* **Python 3.x**
* **[pybit](https://github.com/bybit-exchange/pybit):** The official Python SDK for the Bybit API.
* **[discord.py](https://github.com/Rapptz/discord.py):** A Python wrapper for the Discord API, used for both monitoring and notifying.
* **[requests](https://pypi.org/project/requests/):** For general HTTP requests.

## Original Setup Instructions (For Archival Only)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Erwann-RAMBEAUX/bot_crypto.git
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install requests pybit discord.py
    ```

3.  **Configure API Keys:** Add your Bybit API keys (key and secret) to the `constant.py` file.

4.  **Configure Discord Bot:**
    * Create a Discord Bot application in the Discord Developer Portal.
    * Add the bot's token to `trade.py` (for the listener) and `bot.py` (for the notifier).

## Original Usage (For Archival Only)

1.  **Run the main trading script:**
    ```bash
    python trade.py
    ```
2.  The script would then monitor the target channel. The notifier bot (if used) would need to be run separately:
    ```bash
    python bot.py
    ```

## Disclaimer

This project was provided for educational purposes only. All trading, especially with cryptocurrencies, involves substantial risk. You can lose your entire investment. The author is not responsible for any financial losses incurred from the use or misuse of this code. This software was provided "as-is" with no warranty.
