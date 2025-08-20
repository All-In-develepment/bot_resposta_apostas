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
        
        if domain in ["EstrelaBet", "McGames", "SportingBet", "Lotogreen", "EsportivaBet", "JogoDeOuro", "Novibet"]:
            # Gera botões para escolher o canal de divulgação
            options = ["TELEGRAM", "WHATSAPP", "INSTAGRAM", "BINGO", "TRAFEGO PAGO", "SEM UTM"]
            reply_markup = self.create_buttons(options)
            await update.message.reply_text("📢 Escolha o canal onde você irá divulgar:", reply_markup=reply_markup)
            
            # Salva a mensagem original e o domínio no contexto do usuário
            context.user_data["last_message"] = user_message
            context.user_data["domain"] = domain

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()  # Responde a interação para evitar o erro "Botão carregando..."

        selected_option = query.data  # Obtém a opção escolhida
        user_message = context.user_data.get("last_message", "")
        domain = context.user_data.get("domain", "")

        if user_message and domain:
            # Gera o link com base na opção e na mensagem original
            msg_replay = ""
            
            # Para a opção "SEM UTM", passa None como selected_option
            utm_option = None if selected_option == "SEM UTM" else selected_option
            
            if domain == "EstrelaBet":
                msg_replay = self.bet_link.EstrelaBetLink(user_message, utm_option)
            elif domain == "McGames":
                msg_replay = self.bet_link.McGamesLink(user_message, utm_option)
            elif domain == "SportingBet":
                msg_replay = self.bet_link.SportingBetLink(user_message, utm_option)
            elif domain == "Lotogreen":
                msg_replay = self.bet_link.LotoGreenLink(user_message, utm_option)
            elif domain == "EsportivaBet":
                msg_replay = self.bet_link.EsportivaBetLink(user_message, utm_option)
            elif domain == "JogoDeOuro":
                msg_replay = self.bet_link.JogoDeOuroLink(user_message, utm_option)
            elif domain == "Novibet":
                msg_replay = self.bet_link.NovibetLink(user_message, utm_option)
            
            # Emoji para cada canal
            channel_emoji = {
                "TELEGRAM": "📱",
                "WHATSAPP": "💬", 
                "INSTAGRAM": "📸",
                "BINGO": "🎰",
                "TRAFEGO PAGO": "💰",
                "SEM UTM": "🔗"
            }
            
            emoji = channel_emoji.get(selected_option, "🔗")
            
            if selected_option == "SEM UTM":
                response_text = f"{emoji} Link sem UTM gerado:\n\n{msg_replay}"
            else:
                response_text = f"{emoji} Canal selecionado: {selected_option}\n🔗 Seu link com UTM:\n\n{msg_replay}"
        else:
            response_text = f"Erro: Não foi possível processar sua solicitação. Tente enviar o link novamente."

        await query.message.reply_text(response_text)
