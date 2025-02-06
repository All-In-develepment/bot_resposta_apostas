import os
from dotenv import load_dotenv
import telebot
import time
from Services.user_services import UserService
import Services.message_services as MensagemService
from Services.betting_house import BettingHouse

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variables
token = os.getenv("TELEGRAM_BOT_TOKEN")

# Create a Bot object
bot = telebot.TeleBot(token)

codigos_afiliados = {}
@bot.message_handler(commands=['CadastrarLinkSuperBet'])
def solicitar_codigo(message):
    bot.send_message(message.chat.id, "Por favor, envie o código de afiliado:")
    
    bot.register_next_step_handler(message, salvar_codigo, "SuperBet")
    
@bot.message_handler(commands=['CadastrarLinkBetNacional'])
def solicitar_codigo_bet_nascional(message):
    bot.send_message(message.chat.id, "Por favor, envie o código de afiliado:")
    
    bot.register_next_step_handler(message, salvar_codigo, "BetNacional")

# Lista de comandos disponíveis
comandos = {
    "/CadastrarLinkSuperBet": "Cadastrar um código de afiliado",
    "/CadastrarLinkBetNacional": "Cadastrar um código de afiliado",
    "/help": "Exibir todos os comandos disponíveis",
    "/comandos": "Exibir todos os comandos disponíveis"
}

# Comando para exibir a lista de comandos
@bot.message_handler(commands=['help', 'comandos'])
def listar_comandos(message):
    resposta = "🤖 Comandos disponíveis:\n"
    for comando, descricao in comandos.items():
        resposta += f"{comando} - {descricao}\n"
    bot.send_message(message.chat.id, resposta)

class MensagemHandler:
    """ Handler responsável por interagir com o bot e responder às mensagens. """

    @staticmethod
    @bot.message_handler(func=lambda message: True)
    def handle_message(mensagem):
        """ Recebe mensagens e responde caso seja necessário. """
        user = mensagem.from_user.username
        userName = UserService.get_user(user)
        if (userName == None):
            UserService.register_user(user)
            bot.send_message(mensagem.chat.id, """Não encontri seu cadastro.\n
Digite /CadastrarLinkSuperBet para cadastrar seu codigo de afiliado da SuperBet.\n
ou /CadastrarLinkBetNacional para cadastrar seu codigo de afiliado da BetNacional.""")


        if (userName != None):
            bot.send_message(mensagem.chat.id, "Olá, tudo bem?")
        
        if ("http://" in mensagem.text or "https://" in mensagem.text):
            resposta, casa = MensagemService.MensagemService.processar_mensagem(mensagem)
            if resposta:
                bot.send_message(mensagem.chat.id, resposta)
                time_now = time.strftime("%d/%m/%Y %H:%M:%S")
                print(f"[{time_now}] - Respondi para {mensagem.from_user.username}: {casa}")
        else:
            bot.send_message(mensagem.chat.id, "Por favor, envie um link válido.")

def salvar_codigo(message, betting_house):
    user_id = message.from_user.id
    codigos_afiliados[user_id] = message.text
    print(betting_house)
    if betting_house == "SuperBet":
        BettingHouse.register_link_superbet(message.text, message.from_user.username)
    
    if betting_house == "BetNacional":
        BettingHouse.register_link_betnascinal(message.text, message.from_user.username)
    bot.send_message(message.chat.id, f"Código de afiliado {message.text} salvo com sucesso!")
    
# Iniciar o bot
if __name__ == "__main__":
    bot.polling()
