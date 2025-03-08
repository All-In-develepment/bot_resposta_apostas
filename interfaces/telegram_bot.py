from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from usecases.echo_message import EchoMessageUseCase
from usecases.extract_domain import ExtractDomainUseCase
from usecases.identify_betting import IdentifyBetting
from usecases.bet_link import BetLink
from domain.entities import Message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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
        
        self.application.add_handler(CallbackQueryHandler(self.handle_button_click))

        # Inicia o bot
        self.application.run_polling()
    
    def create_buttons(self, options: list):
        buttons = [[InlineKeyboardButton(option, callback_data=option)] for option in options]
        return InlineKeyboardMarkup(buttons)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text.strip()
        domain = self.identify_betting.IdentifyBetting(user_message)
        if domain == "EstrelaBet":
            # Gera aposta da EstrelaBet
            # Gera botões para escolher a plataforma
            options = ["INSTAGRAM / STORY", "INSTAGRAM / REELS", "TELEGRAM", "WHATSAPP", "TRAFEGO PAGO", "DISPARO", "YOUTUBE"]
            reply_markup = self.create_buttons(options)
            await update.message.reply_text("Choose an option:", reply_markup=reply_markup)
            
            # Salva a mensagem original no contexto do usuário
            context.user_data["last_message"] = user_message
            
            # msg_replay = self.bet_link.EstrelaBetLink(user_message)
            # await update.message.reply_text(f"{msg_replay}")
        
        if domain == "McGames":
            # Gera aposta da McGames
            msg_replay = self.bet_link.McGamesLink(user_message)
            await update.message.reply_text(f"{msg_replay}")
        
        if domain == "SportingBet":
            # Gera aposta da SportingBet
            msg_replay = self.bet_link.SportingBetLink(user_message)
            await update.message.reply_text(f"{msg_replay}")

        # await update.message.reply_text(f"{domain}")

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()  # Responde a interação para evitar o erro "Botão carregando..."

        selected_option = query.data  # Obtém a opção escolhida
        user_message = context.user_data.get("last_message", "")

        if user_message:
            # Gera o link com base na opção e na mensagem original
            msg_replay = self.bet_link.EstrelaBetLink(user_message, selected_option)
            response_text = f"Você escolheu: {selected_option}\nAqui está seu link: {msg_replay}"
        else:
            response_text = f"Você escolheu: {selected_option}"

        await query.message.reply_text(response_text)
