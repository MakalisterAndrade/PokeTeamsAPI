# Use a imagem Alpine do Python como base
FROM python:3.8-alpine

# Define a variável de ambiente para não gerar logs de saída em buffer
ENV PYTHONUNBUFFERED 1

# Crie o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instale as dependências a partir do arquivo requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copie todo o conteúdo do projeto para o contêiner
COPY . /app

# Expõe a porta que a aplicação estará escutando (ajuste conforme necessário)
EXPOSE 80

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "main.py"]