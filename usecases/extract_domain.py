from urllib.parse import urlparse

class ExtractDomainUseCase:
    def execute(self, url: str) -> str:
        msg = url.split("https://")
        parsed_url = urlparse(msg)
        if not parsed_url.netloc:
            return "URL inválida"
        return parsed_url.netloc
    
    
