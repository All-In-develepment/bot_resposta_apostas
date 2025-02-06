from Services.betting_house import BettingHouse
from Services.user_services import UserService
class MensagemService:
    """ Serviço responsável por processar mensagens recebidas no bot. """

    @staticmethod
    def processar_mensagem(mensagem):
        """ Determina o tipo de mensagem e gera uma resposta adequada. """
        if "betnacional.bet" in mensagem.text:
            bet_id = BettingHouse.get_betting_house_by_name("BetNacional")['id']
            afiliate_code = BettingHouse.get_user_betting_house(user_id, bet_id)
            return MensagemService._processar_betnacional(mensagem.text, afiliate_code), "BetNacional"

        if "superbet.bet.br/" in mensagem.text:
            bet_id = BettingHouse.get_betting_house_by_name("SuperBet")['id']
            user_id = UserService.get_user(mensagem.from_user.username)['id']
            afiliate_code = BettingHouse.get_user_betting_house(user_id, bet_id)
            return MensagemService._processar_superbet(mensagem.text, afiliate_code), "SuperBet"

        return None  # Retorna None caso a mensagem não seja relevante

    @staticmethod
    def _processar_betnacional(texto, afliate_code):
        """ Processa links da betnacional e retorna a resposta formatada. """
        try:
            bet_code = texto.split("betslip=")[1]
            # codigo_de_afiliado = "EsseAquiÉoSeuCodigoDeAfiliado"
            return f"https://record.betnacional.bet.br/{afliate_code}share?betslip={bet_code}"
        except IndexError:
            return "Erro ao processar o link da BetNacional."

    @staticmethod
    def _processar_superbet(texto, afliate_code):
        """ Processa links da SuperBet e retorna a resposta formatada. """
        try:
            # bet_code = 'btag=a_5602b_378c_&affid=662&siteid=5602&adid=378&c=nalandageral&asclurl='
            return f"{afliate_code}{texto}"
        except IndexError:
            return "Erro ao processar o link da SuperBet."