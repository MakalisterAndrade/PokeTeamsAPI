from flask import Flask, request, jsonify
from app.models import Team
import requests
import json

app = Flask(__name__)

teams = {}  # Dicionário para armazenar os times

def get_pokemon_data(pokemon_name):
    # Faz uma solicitação à pokeapi.co para obter os dados do Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code != 200:
        return None  # Pokemon não encontrado

    data = response.json()
    pokemon_id = data.get("id")
    height = data.get("height")
    weight = data.get("weight")

    return {
        "id": pokemon_id,
        "height": height,
        "weight": weight
    }

@app.route('/api/teams', methods=['GET'])
def get_teams():
    teams_list = [team.to_dict() for team in teams.values()]
    return jsonify(teams_list)


@app.route('/api/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = teams.get(team_id)
    if not team:
        return jsonify({"error": "Time não encontrado"}), 404
    return jsonify(team.to_dict())  # Usar o método to_dict para serializar o objeto Team como Json
@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    user = data.get('user')
    team_data = data.get('team')

    if not user or not team_data:
        return jsonify({"error": "Entrada inválida"}), 400

    # Verifica se o user já existe em algum time
    for team_id, existing_team in teams.items():
        if existing_team.owner == user:
            return jsonify({"error": f"O user {user} já existe para o time {team_id}"}), 400

    pokemons = []
    for pokemon_name in team_data:
        # Valida e obtém os dados do Pokémon
        pokemon_data = get_pokemon_data(pokemon_name)

        if pokemon_data is None:
            return jsonify({"error": f"Pokemon {pokemon_name} não existe"}), 400

        pokemons.append({
            "id": pokemon_data["id"],
            "name": pokemon_name,
            "weight": pokemon_data["weight"],
            "height": pokemon_data["height"]
        })

    new_team = Team(owner=user, pokemons=pokemons)
    team_id = len(teams) + 1
    teams[team_id] = new_team

    # Aqui retorna uma mensagem personalizada ao usuário
    return jsonify({"message": f"Time registrado com sucesso. O ID a ser passado para pesquisa é: {team_id}"})

if __name__ == '__main__':
    app.run(debug=True)
