from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        'nome':'eu sei que vem',
        'autor':'Isadora Pompoe'
    },
    {
        'nome':'hino da vitória',
        'autor':'Cassiane'
    },
    {
        'nome':'escudo',
        'autor':'Voz da Verdade'
    },
]

@app.route('/')
def obter_musicas():
    return jsonify(musicas)

@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musicas_pelo_id(indice):
    return jsonify(musicas[indice])

@app.route('/musicas', methods=['POST'])
def criar_nova_musica():
    try:
        musica = request.get_json()
        musicas.append(musica)

        return jsonify(musica, 200)
    except:
        return jsonify('Verifique sua requisição', 400)

@app.route('/musicas/<int:indice>', methods=['PUT'])
def atualizar_musica(indice):
    try:
        musica = request.get_json()
        musicas[indice].update(musica)

        return jsonify(musicas[indice],200)
    except:
        return jsonify('Verifique sua requisição', 400)

@app.route('/musicas/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluído a postagem {musicas[indice]}',200)
    except:
        return jsonify('Verifique sua requisição', 400)
        
app.run(port=5000, host='localhost', debug=True)    