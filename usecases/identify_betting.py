class IdentifyBetting:
    def IdentifyBetting(self, url: str) -> str:
        if "estrelabet" in url:
            return "EstrelaBet"

        if "mcgames" in url:
            return "McGames"
        # Identify betting
        
        if "sportingbet" in url:
            # https://sports.sportingbet.bet.br/pt-br/share-my-bet/9a4c098d57
            return "SportingBet"

        if "lotogreen" in url:
            return "Lotogreen"
        
        if "esportiva.bet" in url:
            return "EsportivaBet"
        
        if "jogodeouro.bet.br" in url:
            return "JogoDeOuro"
        
        if "novibet.bet" in url:
            return "Novibet"

        return "casa indefinida"