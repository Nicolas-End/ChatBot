from flask import render_template, Flask, request, jsonify
import cohere_connection.co as co 
import json;
chatbot=co.ChatBot()
#Pega todos os presets do ChatBot
with open('Presets_to_cohere.json', 'r') as presets_from_json:
        presets = json.load(presets_from_json)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#recebe os dados Do formulario Html
@app.route('/home', methods=['POST'])
def home():
    #recebe a pergunta do usuario
    input_from_user = request.form['input_from_user']
    response_from_cohere = chatbot.response_from_cohere(input_from_user,presets)

    #retorna para o arquivo static/main.js em formato json
    return jsonify(response_from_cohere)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)