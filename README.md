# Desafio Outsera

## Pré-requisitos
- Python 3.8 ou superior
- Java 21 (para o banco de dados H2)

## Instalação
- Criar um ambiente virtual com o comando `python -m venv venv`.
- Ativar o ambiente virtual:
  - No Windows (cmd): `venv\Scripts\activate.bat`
  - No Linux/Mac: `source venv/bin/activate`
- Executar o comando `pip install -r requirements.txt` para instalar as dependências do projeto.

## Execução
- O projeto irá carregar o banco de dados a partir do arquivo `resources/movielist.csv`.
  - Se necessário, altere esse arquivo para adicionar ou remover filmes.
- Para executar o projeto, utilize o comando `python src/main.py`.
- Navegar até `http://127.0.0.1:8000/raspberry-awards/` para acessar a funcionalidade requisitada.

## Testes de Integração
- Para executar os testes, utilize o comando `pytest` na raiz do projeto.

