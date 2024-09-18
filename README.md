# PokeTeamsAPI
## Documentação da API PokeTeams

Este é um guia de documentação para a API PokeTeams, que permite criar e listar times de Pokémons, utilizando a PokeAPI(https://pokeapi.co/). A documentação inclui instruções para inicializar o projeto com Docker, como usar a API localmente e no Docker Compose, e informações detalhadas sobre cada rota da API com exemplos de entrada e saída.

## Inicialização com Docker

Se você não possui o Docker instalado, siga as instruções em [Docker Installation Guide](https://docs.docker.com/compose/install/) para instalar o Docker em seu sistema.

### Inicialização com Docker Compose

1. Clone o repositório do projeto:
```bash
git clone https://github.com/MakalisterAndrade/PokeTeamsAPI.git
```
```bash
cd PokeTeamsAPI
```
2. Dentro do diretório do projeto, execute o seguinte comando para iniciar a aplicação com Docker Compose:
```bash
docker-compose up
```
Isso iniciará a API e a disponibilizará em http://localhost:5000.

### Uso Local

Para usar a API localmente sem Docker, siga as etapas a seguir:

1. Clone o repositório do projeto:
```bash
git clone https://github.com/MakalisterAndrade/PokeTeamsAPI.git
```
```bash
cd PokeTeamsAPI
```

2. Instale as dependências do Python:

```bash
pip install -r requirements.txt
```

3. Inicie a aplicação localmente:

```bash
python main.py
```
A API estará disponível em http://localhost:5000.

## Rotas da API

Para testar esta API, você pode usar ferramentas como [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/) ou [Curl](https://curl.se/).

Aqui estão alguns exemplos de uso das rotas da API:

### Listar Todos os Times (GET /api/teams)

- **Descrição**: Retorna uma lista de todos os times registrados.

- **Exemplo de Requisição**:
  
```bash
curl -X GET http://localhost:5000/api/teams
```

- **Exemplo de Resposta**:

```json
[
	{
		"owner": "sleao",
		"pokemons": [
			{
				"height": 16,
				"id": 9,
				"name": "blastoise",
				"weight": 855
			},
			{
				"height": 4,
				"id": 25,
				"name": "pikachu",
				"weight": 60
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			},
			{
				"height": 20,
				"id": 3,
				"name": "venusaur",
				"weight": 1000
			},
			{
				"height": 25,
				"id": 131,
				"name": "lapras",
				"weight": 2200
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			}
		]
	},
	{
		"owner": "maka",
		"pokemons": [
			{
				"height": 16,
				"id": 9,
				"name": "blastoise",
				"weight": 855
			},
			{
				"height": 4,
				"id": 25,
				"name": "pikachu",
				"weight": 60
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			}
		]
	}
]

```

### Buscar Time por ID (GET /api/teams/{id})


- **Descrição**: Retorna um time registrado com base em sua ID única.
  
- **Exemplo de Requisição**: 
```bash 
curl -X GET http://localhost:5000/api/teams/1
```

- **Exemplo de Resposta**: 
```json
{
	"owner": "sleao",
	"pokemons": [
		{
			"height": 16,
			"id": 9,
			"name": "blastoise",
			"weight": 855
		},
		{
			"height": 4,
			"id": 25,
			"name": "pikachu",
			"weight": 60
		},
		{
			"height": 17,
			"id": 6,
			"name": "charizard",
			"weight": 905
		},
		{
			"height": 20,
			"id": 3,
			"name": "venusaur",
			"weight": 1000
		},
		{
			"height": 25,
			"id": 131,
			"name": "lapras",
			"weight": 2200
		},
		{
			"height": 17,
			"id": 6,
			"name": "charizard",
			"weight": 905
		}
	]
}
```

### Criar Time (POST /api/teams)


- **Descrição**: Cria um novo time com base em uma lista de Pokémons e um nome de usuário.
  
- **Exemplo de Requisição**: 
```bash 
curl -X POST -H "Content-Type: application/json" -d '{
  "user": "sleao",
  "team": ["blastoise", "pikachu", "charizard", "venusaur", "lapras", "charizard"]
}' http://localhost:5000/api/teams
```

- **Exemplo de Resposta**: 
```json
{
	"message": "Time registrado com sucesso. O ID a ser passado para pesquisa é: 1"
}
```
API criada para o desafio de infraestrutura da Triágil. 

[Link para o Desafio Infra Triágil](https://github.com/triagilbr/desafio-infra-triagil)
