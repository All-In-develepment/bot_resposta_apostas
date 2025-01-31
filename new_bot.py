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

# Função principal para responder às mensagens
@bot.message_handler()
def responder(mensagem):
    if ("betnacional.bet" in mensagem.text):
        bet_code = mensagem.text.split("betslip=")[1]
        codigo_de_afiliado = "EsseAquiÉoSeuCodigoDeAfiliado"
        resposta = f"https://record.betnacional.bet.br/{codigo_de_afiliado}/1/share?betslip={bet_code}"
        bot.send_message(mensagem.chat.id, resposta)
        print(f"Respondi para {mensagem.from_user.username}: {resposta}")
    
    if ("superbet.bet.br/" in mensagem.text):
        '''
            Exemplos:
            recebe: https://superbet.bet.br/bilhete-compartilhado/898F-7T3ZUZ
            retorno: https://wlsuperbet.adsrv.eacdn.com/C.ashx?btag=a_5602b_378c_&affid=662&siteid=5602&adid=378&c=nalandageral&asclurl=https://superbet.bet.br/bilhete-compartilhado/898F-7T3ZUZ
        '''
        bet_code = mensagem.text.split("bilhete-compartilhado/")[1]
        codigo_de_afiliado = "EsseAquiÉoSeuCodigoDeAfiliado"
        resposta = f"https://wlsuperbet.adsrv.eacdn.com/C.ashx?btag=a_5602b_378c_&affid=662&siteid=5602&adid=378&c=nalandageral&asclurl={mensagem.text}"
        bot.send_message(mensagem.chat.id, resposta)
        print(f"Respondi para {mensagem.from_user.username}: {resposta}")

# Iniciar o bot
bot.polling()
