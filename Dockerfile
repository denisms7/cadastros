# Imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o restante do projeto para o diretório de trabalho
COPY . .

# Expõe a porta 8000 (ou qualquer porta usada pelo Django)
EXPOSE 8000

# Define o comando para executar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
