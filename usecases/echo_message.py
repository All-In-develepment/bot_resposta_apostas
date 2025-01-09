from domain.entities import Message

class EchoMessageUseCase:
    def execute(self, message: Message) -> Message:
        # Retorna o mesmo texto
        return message
