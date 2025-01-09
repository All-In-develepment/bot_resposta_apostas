from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from usecases.echo_message import EchoMessageUseCase
from usecases.extract_domain import ExtractDomainUseCase
from usecases.identify_betting import IdentifyBetting
from usecases.bet_link import BetLink
from domain.entities import Message

class TelegramBot:
    def __init__(self, token: str):
        # Substituímos o Updater pelo Application.builder
        self.application = Application.builder().token(token).build()
        self.echo_usecase = EchoMessageUseCase()
        self.extract_domain_usecase = ExtractDomainUseCase()
        self.identify_betting = IdentifyBetting()
        self.bet_link = BetLink()

    def start(self):
        # Adicionamos o handler para processar mensagens
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Inicia o bot
        self.application.run_polling()

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text.strip()
        domain = self.identify_betting.IdentifyBetting(user_message)
        if domain == "EstrelaBet":
            # Gera aposta da EstrelaBet
            msg_replay = self.bet_link.EstrelaBetLink(user_message)
            await update.message.reply_text(f"{msg_replay}")
        
        if domain == "McGames":
            # Gera aposta da McGames
            msg_replay = self.bet_link.McGamesLink(user_message)
            await update.message.reply_text(f"{msg_replay}")

        await update.message.reply_text(f"{domain}")
