# Use a imagem base do Python
FROM python:3.12

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo de requisitos para o contêiner
COPY requirements.txt .

RUN apt-get update && apt-get install -y

# Instalando as dependências da aplicação
RUN pip install -r requirements.txt

# Copiando todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# EXPOSE 8000

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "-u", "new_bot.py"]