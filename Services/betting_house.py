import requests
import os
from dotenv import load_dotenv

from Services.user_services import UserService

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# URL base da API
base_url = os.getenv("API_BASE_URL")

class BettingHouse:
    """Serviços relacionados à casa de apostas."""
    
    @staticmethod
    def register_link_betnascinal(afiliate_code, user_name):
        """Cadastra o codigo de afiliado ca Bet Nascinal"""
        try:
            user_id = UserService.get_user(user_name)["id"]
            bet_id = BettingHouse.get_betting_house_by_name("BetNacional")["id"]
            
            endpoint = f"{base_url}/TelegramUser"
            data = {
                "AfiliateCode": afiliate_code,
                "BettingHouseId": user_id,
                "TelegramUserId": bet_id
            }
            
            requests.post(endpoint, json=data)
        except IndexError:
            return "Houve um erro ao cadastrar o código de afiliado da BetNascinal."

    @staticmethod
    def register_link_superbet(afiliate_code):
        """Processa links da SuperBet e retorna a resposta formatada."""
        try:
            bet_code = 'btag=a_5602b_378c_&affid=662&siteid=5602&adid=378&c=nalandageral&asclurl='
            return f"https://wlsuperbet.adsrv.eacdn.com/C.ashx?{bet_code}={afiliate_code}"
        except IndexError:
            return "Erro ao processar o link da SuperBet."
    
    @staticmethod
    def get_betting_house_by_name(name):
        """Retorna a casa de apostas pelo nome."""
        endpoint = f"{base_url}/BettingHouse/{name}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None