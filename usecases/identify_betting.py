class IdentifyBetting:
    def IdentifyBetting(self, url: str) -> str:
        if "estrelabet" in url:
            return "EstrelaBet"

        if "mcgames" in url:
            return "McGames"
        # Identify betting
        return "casa indefinida"