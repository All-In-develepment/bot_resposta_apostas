# Exemplos de UTMs por Canal

## Como funciona:

1. **Usuário envia um link de aposta**
2. **Bot identifica a casa de apostas**
3. **Bot pergunta qual canal será usado para divulgação**
4. **Bot gera o link final com UTM específica OU sem UTM**

## Opções disponíveis:

### TELEGRAM
```
utm_source=telegram&utm_medium=social&utm_campaign=apostas
```

### WHATSAPP  
```
utm_source=whatsapp&utm_medium=social&utm_campaign=apostas
```

### INSTAGRAM
```
utm_source=instagram&utm_medium=social&utm_campaign=apostas
```

### SEM UTM
```
Link tratado sem parâmetros UTM (link limpo)
```

## Exemplo prático para EstrelaBet:

**Link original:** `https://sports.estrelabet.com/shareCode=ABC123`

**Links finais:**
- **Telegram:** `https://go.aff.estrelabetpartners.com/SEU_CODIGO?utm_source=telegram&utm_medium=social&utm_campaign=apostas&aposta=ABC123`
- **WhatsApp:** `https://go.aff.estrelabetpartners.com/SEU_CODIGO?utm_source=whatsapp&utm_medium=social&utm_campaign=apostas&aposta=ABC123`
- **Instagram:** `https://go.aff.estrelabetpartners.com/SEU_CODIGO?utm_source=instagram&utm_medium=social&utm_campaign=apostas&aposta=ABC123`
- **Sem UTM:** `https://go.aff.estrelabetpartners.com/SEU_CODIGO?&aposta=ABC123`

## Casas de apostas suportadas:
- ✅ EstrelaBet
- ✅ McGames
- ✅ SportingBet
- ✅ LotoGreen
- ✅ EsportivaBet
- ✅ JogoDeOuro
- ✅ Novibet

Todas as casas agora perguntam sobre o canal antes de gerar o link final com as UTMs apropriadas ou sem UTM.

## Vantagens da opção "SEM UTM":
- ✅ Link mais limpo e curto
- ✅ Melhor para compartilhamento em alguns contextos
- ✅ Ainda mantém o código de afiliado
- ✅ Funciona para todas as casas de apostas
