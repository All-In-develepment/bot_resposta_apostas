import telebot
from verificar_mensagem import verificar_mensagem

# Defina o token de acesso do seu bot
token = "6866021355:AAF9AzKPMn6qFt188VhsyGjE7eQlE2FPmdo"

# Crie um objeto Bot
bot = telebot.TeleBot(token)

# Crie uma função para responder às mensagens
@bot.message_handler()
def responder(mensagem):
    resposta = verificar_mensagem(mensagem.text)
    bot.reply_to(mensagem, resposta)

# Adicione um listener para receber mensagens
# bot.on_message(responder)

# Inicie o bot
bot.polling()
