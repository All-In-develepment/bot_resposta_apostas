class MensagemService:
    """ Serviço responsável por processar mensagens recebidas no bot. """

    @staticmethod
    def processar_mensagem(mensagem):
        """ Determina o tipo de mensagem e gera uma resposta adequada. """
        if "betnacional.bet" in mensagem.text:
            return MensagemService._processar_betnacional(mensagem.text), "BetNacional"

        if "superbet.bet.br/" in mensagem.text:
            return MensagemService._processar_superbet(mensagem.text), "SuperBet"

        return None  # Retorna None caso a mensagem não seja relevante

    @staticmethod
    def _processar_betnacional(texto):
        """ Processa links da betnacional e retorna a resposta formatada. """
        try:
            bet_code = texto.split("betslip=")[1]
            codigo_de_afiliado = "EsseAquiÉoSeuCodigoDeAfiliado"
            return f"https://record.betnacional.bet.br/{codigo_de_afiliado}/1/share?betslip={bet_code}"
        except IndexError:
            return "Erro ao processar o link da BetNacional."

    @staticmethod
    def _processar_superbet(texto):
        """ Processa links da SuperBet e retorna a resposta formatada. """
        try:
            bet_code = 'btag=a_5602b_378c_&affid=662&siteid=5602&adid=378&c=nalandageral&asclurl='
            return f"https://wlsuperbet.adsrv.eacdn.com/C.ashx?{bet_code}={texto}"
        except IndexError:
            return "Erro ao processar o link da SuperBet."