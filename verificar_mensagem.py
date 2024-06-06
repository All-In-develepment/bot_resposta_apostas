def gerar_botoes():
    botoes = [
        ["MONTE SEU BILHETE", "CANAL INSTA"],
        ["STORYS", "FUTEBOL FREE"],
        ["FUTEBOL VIP", "ODDS ALTAS"],
        ["NBA FREE", "NBA VIP"],
        ["YOUTUBE"]
    ]
    return botoes

def verificar_mensagem(mensagem, afiate_code):
    codigo = None
    if "shareCode=" in mensagem:
        codigo = mensagem.split("shareCode=")[1]
        mensagem = mensagem.split("https://")[0]  # Remover link da mensagem

    if codigo:
        resposta = f"https://go.aff.estrelabetpartners.com/{afiate_code}?aposta={codigo}"
        # botoes = gerar_botoes()
        return codigo,resposta, None
    
    elif mensagem == "Tchau":
        resposta = "Tchau, até mais!"
        return None, resposta, None
    else:
        resposta = "Por favor, compartilhe o link com o código da aposta."
        return None, resposta, None

def obter_resposta_botao(botao):
    respostas = {
        "MONTE SEU BILHETE": "Você escolheu MONTE SEU BILHETE.",
        "CANAL INSTA": "Você escolheu CANAL INSTA.",
        "STORYS": "Você escolheu STORYS.",
        "FUTEBOL FREE": "Você escolheu FUTEBOL FREE.",
        "FUTEBOL VIP": "Você escolheu FUTEBOL VIP.",
        "ODDS ALTAS": "Você escolheu ODDS ALTAS.",
        "NBA FREE": "Você escolheu NBA FREE.",
        "NBA VIP": "Você escolheu NBA VIP.",
        "YOUTUBE": "Você escolheu YOUTUBE."
    }
    return respostas.get(botao, "Opção inválida.")
