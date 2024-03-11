# Copie-Trading Crypto sur Bybit des trade de CryptoPicsou

Ce projet consistait en un script Python permettant de réaliser du copie-trading sur la plateforme Bybit en se basant sur les signaux de trading postés par "CryptoPicsou" sur Discord. Le script est accompagné d'un bot Discord qui annonce automatiquement chaque nouveau trade lancé sur un canal spécifié.

⚠️ **Ce bot n'est plus fonctionnel. Ce README est fourni à titre informatif uniquement.**

## Fonctionnalités

- Surveillance en temps réel des messages postés par "CryptoPicsou" sur Discord.
- Analyse des signaux de trading pour détecter les opportunités d'achat ou de vente.
- Exécution automatique des trades sur la plateforme Bybit en fonction des signaux reçus.
- Notification instantanée des nouveaux trades via un bot Discord.

## Configuration requise

- Python 3.x
- Bibliothèques Python : `requests`, `pybit`, `discord.py`

## Installation

1. **Clonez ce dépôt sur votre machine :**

   ```
   git clone https://github.com/Erwann-RAMBEAUX/bot_crypto.git
   ```

2. **Installez les dépendances Python nécessaires :**

   ```
   pip install requests
   pip install pybit
   pip install discord.py
   ```

3. **Configurez vos clés d'API Bybit dans le fichier `constant.py`.**

4. **Créez un bot Discord et configurez-le pour votre serveur Discord.**

5. **Ajoutez le token du bot Discord dans `trade.py` et `bot.py`.**

## Utilisation

1. **Lancez le script principal `trade.py` :**

   ```
   python trade.py
   ```

2. **Assurez-vous que le bot Discord est en ligne et a accès au canal spécifié.**

3. **Détendez-vous et laissez le script gérer vos trades en fonction des signaux de "CryptoPicsou" !**

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet ou ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une pull request.

## Avertissement

Ce projet est fourni à titre éducatif uniquement. Le trading de cryptomonnaies comporte des risques et vous pouvez perdre tout votre investissement. Assurez-vous de comprendre les risques associés au trading avant d'utiliser ce logiciel.

## Auteurs

- [Erwann RAMBEAUX](https://github.com/Erwann-RAMBEAUX)