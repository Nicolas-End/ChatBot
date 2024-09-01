from flask import render_template, Flask, request, jsonify
import ChatBot as cb
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#recebe os dados Do formulario Html
@app.route('/home', methods=['POST'])
def home():
    entrada = request.form['entrada']
    if entrada !=  "":
        resposta = cb.central(entrada)
    else:
        resposta = 'Ops, você não digitou nada :('
    #Envia os dados para o arquivo javascript
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)