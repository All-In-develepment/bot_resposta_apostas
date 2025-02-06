import requests
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# URL base da API
base_url = os.getenv("API_BASE_URL")

class UserService:
    @staticmethod
    def get_user(username):
        endpoint = f"{base_url}/TelegramUser/{username}"
        response = requests.get(endpoint)
        # UserService.register_user(username)
        if response.status_code == 200:
            return response.json()
        return None
    
    @staticmethod
    def register_user(username):
        endpoint = f"{base_url}/TelegramUser"
        data = {
            "UserTelegramName": username
        }
        response = requests.post(endpoint, json=data)
        return response.status_code == 201