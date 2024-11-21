import os
from dotenv import load_dotenv
import telebot
from telebot import types
from verificar_mensagem import verificar_mensagem

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do bot das variáveis de ambiente
token = os.getenv("TELEGRAM_BOT_TOKEN")

# Criar um objeto Bot
try:
    bot = telebot.TeleBot(token)
except Exception as e:
    # Salvar o erro em um arquivo de log
    with open("log.txt", "a") as arquivo:
        arquivo.write(str(e) + "\n")
    print(f"Ocorreu um erro ao criar o bot: {e}")

# Função para obter o destino após o código de aposta
def obter_destino(mensagem, codigo_aposta):
    try:
        # Obter o código de afiliado enviado pelo cliente
        codigo_afiliado = mensagem.text.strip()

        # Montar o link no formato desejado
        base_url = "https://go.aff.mcgames.bet/"
        link = f"{base_url}{codigo_afiliado}?shareCode={codigo_aposta}"

        # Enviar o link gerado para o cliente
        bot.send_message(mensagem.chat.id, f"Aqui está o link gerado: {link}")
        print(f"Link gerado para {mensagem.from_user.username}: {link}")
    except Exception as e:
        # Salvar o erro em um arquivo de log
        with open("log.txt", "a") as arquivo:
            arquivo.write(str(e) + "\n")
        print(f"Ocorreu um erro ao lidar com o código de afiliado para {mensagem.from_user.username}: {e}")

# Função principal para responder às mensagens
@bot.message_handler()
def responder(mensagem):
    try:
        # Verificar se a mensagem contém o código de aposta
        codigo_aposta, resposta = verificar_mensagem(mensagem.text)

        if codigo_aposta:
            # Solicitar o código de afiliado
            bot.send_message(mensagem.chat.id, resposta)
            bot.register_next_step_handler(mensagem, obter_destino, codigo_aposta)
        else:
            # Caso não haja código de aposta, responder diretamente
            bot.send_message(mensagem.chat.id, resposta)

        print(f"Respondi para {mensagem.from_user.username}: {resposta}")
    except Exception as e:
        # Salvar o erro em um arquivo de log
        with open("log.txt", "a") as arquivo:
            arquivo.write(str(e) + "\n")
        print(f"Ocorreu um erro ao responder a {mensagem.from_user.username}: {e}")

# Iniciar o bot
bot.polling()
