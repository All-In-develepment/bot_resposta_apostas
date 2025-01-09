from interfaces.telegram_bot import TelegramBot
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    bot = TelegramBot(TOKEN)
    bot.start()
