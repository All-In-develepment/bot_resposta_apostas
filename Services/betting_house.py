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
        user_name = UserService.get_user(user_name)["id"]
        bet_id = BettingHouse.get_betting_house_by_name("BetNacional")
        
        if bet_id == None:
            BettingHouse.register_betting_house("BetNacional")
            bet_id = BettingHouse.get_betting_house_by_name("BetNacional")["id"]
        if bet_id:
            bet_id = bet_id["id"]
            BettingHouse.register_betting_user(user_name, bet_id, afiliate_code)

    @staticmethod
    def register_link_superbet(afiliate_code, user_name):
        """Processa links da SuperBet e retorna a resposta formatada."""
        user_name = UserService.get_user(user_name)["id"]
        bet_id = BettingHouse.get_betting_house_by_name("SuperBet")
        
        if bet_id == None:
            BettingHouse.register_betting_house("SuperBet")
            bet_id = BettingHouse.get_betting_house_by_name("SuperBet")["id"]
        if bet_id:
            bet_id = bet_id["id"]
            BettingHouse.register_betting_user(user_name, bet_id, afiliate_code)

    
    @staticmethod
    def get_betting_house_by_name(name):
        """Retorna a casa de apostas pelo nome."""
        endpoint = f"{base_url}/BettingHouse/{name}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None
    
    @staticmethod
    def register_betting_house(name):
        """Registra uma nova casa de apostas."""
        endpoint = f"{base_url}/BettingHouse"
        data = {
            "BettingHouseName": name
        }
        response = requests.post(endpoint, json=data)
        return response.status_code == 200
    
    @staticmethod
    def register_betting_user(user_id, betting_house_id, afiliate_code):
        """Registra um novo usuário de uma casa de apostas."""
        endpoint = f"{base_url}/BettingUser"
        data = {
            "TelegramUserId": user_id,
            "BettingHouseId": betting_house_id,
            "AfiliateCode": afiliate_code
        }
        response = requests.post(endpoint, json=data)
        return response.status_code == 200
    
    @staticmethod
    def get_user_betting_house(user_id, betting_house_id):
        """Retorna a casa de apostas de um usuário."""
        endpoint = f"{base_url}/BettingUser/TelegramUserId/{user_id}/BettingHouseId/{betting_house_id}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()['afiliateCode']
        return None