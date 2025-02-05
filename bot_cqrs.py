import os
from dotenv import load_dotenv
import telebot
import time
import Services.user_services as UserService
import Services.message_services as MensagemService

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
    
    bot.register_next_step_handler(message, salvar_codigo)

# Lista de comandos disponíveis
comandos = {
    "/CadastrarLinkSuperBet": "Cadastrar um código de afiliado",
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
        userName = UserService.UserService.get_user(user)
        if (userName == None):
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

def salvar_codigo(message):
    user_id = message.from_user.id
    codigos_afiliados[user_id] = message.text
    bot.send_message(message.chat.id, f"Código de afiliado {message.text} salvo com sucesso!")
    
# Iniciar o bot
if __name__ == "__main__":
    bot.polling()
