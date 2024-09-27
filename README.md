## IA LANGCHAIN

Este projeto é um compilador escrito em python.

Clone este repositorio git em seu computador

 > git clone https://github.com/mhmartins00/ia-langchain.git

 > git checkout main


## Configuration

Crie um ambiente virtual
 > python -m venv .env

Ative este ambiente virtual
 > .env/Scripts/activate

## Installation

Instale as dependencias
 > pip install -r requirements.txt


No arquivo main, altere o conteudo de `query` para realizar a sua pergunta.

    from langchain import executeQuestion

    query: str = 'Quanto é 3 * 5?' // Insira aqui sua pergunta

    result = executeQuestion(query)

    print(result)

Depois rode o seguinte comando para compilar o arquivo comp.txt
 > python main.py
