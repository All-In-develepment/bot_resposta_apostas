import requests
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class BetLink:
    def EstrelaBetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ESTRELA_BET")

        codigo = url.split("shareCode=")[1]

        link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?&aposta={codigo}"

        return link
    
    def McGamesLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_MCGAMES")
        
        base_url = "https://mcgames.bet.br/sports?bscode="
        codigo_aposta = url.split("bscode=")[1] # Extrair apenas o código
        # https://mcgames.bet.br/sports?bscode=CODIGOBILHETE&utm_source=IDAFILIADO
        link = f"{base_url}{codigo_aposta}&utm_source={afiliate_code}"
        return link
        # link = f"{base_url}{afiliate_code}?shareCode={codigo_aposta}"
    
    def SportingBetLink(self, url: str) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_SPORTING_BET")
        
        base_url = os.getenv("API_TRACE_LINK_URL")
        final_url = requests.get(base_url + url).json()
        
        if (final_url['redirectedUrl'] == None):
            return "Houve um erro ao gerar o link, tente novamente mais tarde"
        
        return f"{final_url['redirectedUrl']}&wm={afiliate_code}"