def verificar_mensagem(mensagem):
    """
    Verifica se a mensagem contém o código de aposta e retorna a resposta adequada.
    """
    codigo_aposta = None

    # Verificar se há um código de aposta no link
    if "shareCode=" in mensagem:
        codigo_aposta = mensagem.split("shareCode=")[1].split("&")[0]  # Extrair apenas o código
        resposta = "Código de aposta recebido! Agora, por favor, envie o link contendo o código de afiliado."
        return codigo_aposta, resposta

    # Respostas padrões para mensagens inválidas
    if mensagem.lower() == "tchau":
        return None, "Tchau, até mais!"
    
    return None, "Por favor, compartilhe o link contendo o código de aposta."

