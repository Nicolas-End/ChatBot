from flask import render_template, Flask, request, jsonify
import co 
import json;
chatbot=co.ChatBot()
with open('Dados.json', 'r') as dc:
        dados = json.load(dc)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#recebe os dados Do formulario Html
@app.route('/home', methods=['POST'])
def home():
    entrada = request.form['entrada']
    resposta = chatbot.resposta_cohere(entrada,dados)
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)