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

        return "casa indefinida"