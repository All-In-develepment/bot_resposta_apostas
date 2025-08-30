import requests
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class BetLink:
    def EstrelaBetLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ESTRELA_BET")
        codigo = url.split("aposta=")[1]

        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?utm_source=telegram&utm_medium=social&utm_campaign=apostas&aposta={codigo}"
            elif selected_option == "WHATSAPP":
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&aposta={codigo}"
            elif selected_option == "INSTAGRAM":
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?utm_source=instagram&utm_medium=social&utm_campaign=apostas&aposta={codigo}"
            elif selected_option == "BINGO":
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?utm_source=bingo&utm_medium=game&utm_campaign=apostas&aposta={codigo}"
            elif selected_option == "TRAFEGO PAGO":
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&aposta={codigo}"
            else:
                link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?&aposta={codigo}"
        else:
            link = f"https://go.aff.estrelabetpartners.com/{afiliate_code}?&aposta={codigo}"
        
        return link
    
    def McGamesLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_MCGAMES")
        codigo_aposta = url.split("shareCode=")[1]
        
        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?utm_source=telegram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}&home=1"
            elif selected_option == "WHATSAPP":
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}&home=1"
            elif selected_option == "INSTAGRAM":
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?utm_source=instagram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}&home=1"
            elif selected_option == "BINGO":
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?utm_source=bingo&utm_medium=game&utm_campaign=apostas&shareCode={codigo_aposta}&home=1"
            elif selected_option == "TRAFEGO PAGO":
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&shareCode={codigo_aposta}&home=1"
            else:
                link = f"https://go.aff.mcgames.bet/{afiliate_code}?shareCode={codigo_aposta}&home=1"
        else:
            link = f"https://go.aff.mcgames.bet/{afiliate_code}?shareCode={codigo_aposta}&home=1"
        
        return link
    
    def SportingBetLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_SPORTING_BET")
        
        base_url = os.getenv("API_TRACE_LINK_URL")
        final_url = requests.get(base_url + url).json()
        
        if (final_url['redirectedUrl'] == None):
            return "Houve um erro ao gerar o link, tente novamente mais tarde"
        
        if selected_option:
            if selected_option == "TELEGRAM":
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}&utm_source=telegram&utm_medium=social&utm_campaign=apostas"
            elif selected_option == "WHATSAPP":
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}&utm_source=whatsapp&utm_medium=social&utm_campaign=apostas"
            elif selected_option == "INSTAGRAM":
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}&utm_source=instagram&utm_medium=social&utm_campaign=apostas"
            elif selected_option == "BINGO":
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}&utm_source=bingo&utm_medium=game&utm_campaign=apostas"
            elif selected_option == "TRAFEGO PAGO":
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}&utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas"
            else:
                return f"{final_url['redirectedUrl']}&wm={afiliate_code}"
        else:
            return f"{final_url['redirectedUrl']}&wm={afiliate_code}"
    
    def LotoGreenLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_LOTO_GREEN")
        codigo_aposta = url.split("shareCode=")[1]
        
        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?utm_source=telegram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "WHATSAPP":
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "INSTAGRAM":
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?utm_source=instagram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "BINGO":
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?utm_source=bingo&utm_medium=game&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "TRAFEGO PAGO":
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&shareCode={codigo_aposta}"
            else:
                link = f"https://go.aff.lotogreen.com/{afiliate_code}?shareCode={codigo_aposta}"
        else:
            link = f"https://go.aff.lotogreen.com/{afiliate_code}?shareCode={codigo_aposta}"
        
        return link
    
    def EsportivaBetLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ESPORTIVA_BET")
        codigo_aposta = url.split("shareCode=")[1]
        
        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?utm_source=telegram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "WHATSAPP":
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "INSTAGRAM":
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?utm_source=instagram&utm_medium=social&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "BINGO":
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?utm_source=bingo&utm_medium=game&utm_campaign=apostas&shareCode={codigo_aposta}"
            elif selected_option == "TRAFEGO PAGO":
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&shareCode={codigo_aposta}"
            else:
                link = f"https://go.aff.esportiva.bet/{afiliate_code}?shareCode={codigo_aposta}"
        else:
            link = f"https://go.aff.esportiva.bet/{afiliate_code}?shareCode={codigo_aposta}"
        
        return link

    def JogoDeOuroLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_JOGO_DE_OURO")
        codigo_aposta = url.split("shareCode=")[1]
        
        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?utm_source=telegram&utm_medium=social&utm_campaign=apostas&aposta={codigo_aposta}"
            elif selected_option == "WHATSAPP":
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&aposta={codigo_aposta}"
            elif selected_option == "INSTAGRAM":
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?utm_source=instagram&utm_medium=social&utm_campaign=apostas&aposta={codigo_aposta}"
            elif selected_option == "BINGO":
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?utm_source=bingo&utm_medium=game&utm_campaign=apostas&aposta={codigo_aposta}"
            elif selected_option == "TRAFEGO PAGO":
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&aposta={codigo_aposta}"
            else:
                link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?aposta={codigo_aposta}"
        else:
            link = f"https://go.aff.jogodeouro.bet/{afiliate_code}?aposta={codigo_aposta}"
        
        return link
    
    def NovibetLink(self, url: str, selected_option: str = None) -> str:
        afiliate_code = os.getenv("AFILIATE_CODE_ALFABET")
        
        if selected_option:
            if selected_option == "TELEGRAM":
                link = f"{afiliate_code}&utm_source=telegram&utm_medium=social&utm_campaign=apostas&redirect_url={url}"
            elif selected_option == "WHATSAPP":
                link = f"{afiliate_code}&utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&redirect_url={url}"
            elif selected_option == "INSTAGRAM":
                link = f"{afiliate_code}&utm_source=instagram&utm_medium=social&utm_campaign=apostas&redirect_url={url}"
            elif selected_option == "BINGO":
                link = f"{afiliate_code}&utm_source=bingo&utm_medium=game&utm_campaign=apostas&redirect_url={url}"
            elif selected_option == "TRAFEGO PAGO":
                link = f"{afiliate_code}&utm_source=paid_traffic&utm_medium=ads&utm_campaign=apostas&redirect_url={url}"
            else:
                link = f"{afiliate_code}&redirect_url={url}"
        else:
            link = f"{afiliate_code}&redirect_url={url}"
        
        return link