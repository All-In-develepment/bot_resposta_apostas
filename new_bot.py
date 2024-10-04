import os
from dotenv import load_dotenv, dotenv_values
import telebot
from telebot import types
from verificar_mensagem import verificar_mensagem, obter_resposta_botao

# Carregar as variáveis de ambiente do arquivo .env
config = dotenv_values(".env")
load_dotenv()

# Obter o token do bot das variáveis de ambiente
token = os.getenv("TELEGRAM_BOT_TOKEN")

# Criar um objeto Bot
try:
    bot = telebot.TeleBot(token)
except Exception as e:
    # Salvar o erro em um arquivo de log
    with open("log.txt", "a") as arquivo:
        arquivo.write(str(e))
    print(f"Ocorreu um erro ao criar o bot: {e}")

# Função para enviar os botões de interatividade
def enviar_botoes(chat_id, botoes):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for linha in botoes:
        botoes_formatados = [types.KeyboardButton(botao) for botao in linha]
        markup.add(*botoes_formatados)
    bot.send_message(chat_id, ".", reply_markup=markup)

# Criar uma função para responder às mensagens
@bot.message_handler()
def responder(mensagem):
    try:
        codigo, resposta, botoes = verificar_mensagem(mensagem.text, os.getenv("AFILIATE_CODE"))
        
        # Se houver um código, perguntar o destino
        if codigo:
            # enviar_botoes(mensagem.chat.id, botoes)
            # Salvar o código como uma variável de chat
            bot.send_message(mensagem.chat.id, resposta)
            # bot.register_next_step_handler(mensagem, obter_destino, codigo)
        else:
            # Se não houver código, enviar a resposta
            bot.send_message(mensagem.chat.id, resposta)
        
        print(f"Respondi para {mensagem.from_user.username}: {resposta}")
    except Exception as e:
        # Salvar o erro em um arquivo de log
        with open("log.txt", "a") as arquivo:
            arquivo.write(str(e))
        print(f"Ocorreu um erro ao responder a {mensagem.from_user.username}: {e}")

# Função para obter o destino após o usuário escolher
# def obter_destino(mensagem, codigo):
#     try:
#         resposta = obter_resposta_botao(mensagem.text)
        
        
#         utm_campaign = ""
#         if mensagem.text == "MONTE SEU BILHETE":
#             utm_campaign = "montesb"
#         elif mensagem.text == "CANAL INSTA":
#             utm_campaign = "canalinsta"
#         elif mensagem.text == "STORYS":
#             utm_campaign = "storys"
#         elif mensagem.text == "FUTEBOL FREE":
#             utm_campaign = "futfree"
#         elif mensagem.text == "FUTEBOL VIP":
#             utm_campaign = "futvip"
#         elif mensagem.text == "ODDS ALTAS":
#             utm_campaign = "oddsaltas"
#         elif mensagem.text == "NBA FREE":
#             utm_campaign = "nbafree"
#         elif mensagem.text == "NBA VIP":
#             utm_campaign = "nbavip"
#         elif mensagem.text == "YOUTUBE":
#             utm_campaign = "yt"
        
#         link = f"https://go.aff.estrelabetpartners.com/{os.getenv("AFILIATE_CODE")}?campaign_id=13830&utm_campaign={utm_campaign}&aposta={codigo}"
#         bot.send_message(mensagem.chat.id, link)
#         print(f"Usuário {mensagem.from_user.username} escolheu: {mensagem.text}")
#     except Exception as e:
#         # Salvar o erro em um arquivo de log
#         with open("log.txt", "a") as arquivo:
#             arquivo.write(str(e))
#         print(f"Ocorreu um erro ao lidar com a escolha do botão para {mensagem.from_user.username}: {e}")

# Iniciar o bot
bot.infinity_polling()