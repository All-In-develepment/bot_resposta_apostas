import requests
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class BetLink:
    # def EstrelaBetLink(self, url: str, selected_option) -> str:
    def EstrelaBetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ESTRELA_BET")

        codigo = url.split("shareCode=")[1]

        link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?&aposta={codigo}"
        # link = ""
        # if selected_option == "INSTAGRAM / STORY":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=instagram&utm_term=story?&aposta={codigo}"
        # elif selected_option == "INSTAGRAM / REELS":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=instagram&utm_term=reels?&aposta={codigo}"
        # elif selected_option == "TELEGRAM":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=telegram?&aposta={codigo}"
        # elif selected_option == "WHATSAPP":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=whatsapp?&aposta={codigo}"
        # elif selected_option == "TRAFEGO PAGO":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=tp?&aposta={codigo}"
        # elif selected_option == "DISPARO":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=disparo?&aposta={codigo}"
        # elif selected_option == "YOUTUBE":
        #     link = f"https://go.aff.estrelabetpartners.com/7hfp3csf?utm_term=yt?&aposta={codigo}"
        return link
    
    def McGamesLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_MCGAMES")
        
        codigo_aposta = url.split("shareCode=")[1] # Extrair apenas o código
        link = f"https://go.aff.mcgames.bet/{afiliate_code}?shareCode={codigo_aposta}&home=1"
        return link
    
    def SportingBetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_SPORTING_BET")
        
        base_url = os.getenv("API_TRACE_LINK_URL")
        final_url = requests.get(base_url + url).json()
        
        if (final_url['redirectedUrl'] == None):
            return "Houve um erro ao gerar o link, tente novamente mais tarde"
        
        return f"{final_url['redirectedUrl']}&wm={afiliate_code}"
    
    def LotoGreenLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_LOTO_GREEN")
        
        codigo_aposta = url.split("shareCode=")[1]
        
        # https://go.aff.lotogreen.com/qsp19ap9?shareCode=JNUT8BTXYW
        link = f"https://go.aff.lotogreen.com/{afiliate_code}?shareCode={codigo_aposta}"
        
        return link
    
    def EsportivaBetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ESPORTIVA_BET")
        
        codigo_aposta = url.split("shareCode=")[1]
        
        # https://go.aff.esportivabet.com/3qj2xv8m?shareCode=JNUT8BTXYW
        link = f"https://go.aff.esportiva.bet/{afiliate_code}?shareCode={codigo_aposta}"
        return link

    def JogoDeOuroLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_JOGO_DE_OURO")

        codigo_aposta = url.split("shareCode=")[1]
        
        # https://go.aff.jogodeouro.bet/puie9j8m?shareCode=JNUT8BTXYW
        link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?aposta={codigo_aposta}"
        return link
    
    def NovibetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ALFABET")
        
        link = f"{afiliate_code}&redirect_url={url}"
        return link