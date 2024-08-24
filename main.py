from flask import render_template, Flask, request
import ChatBot as cb
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home():
    entrada = request.form['entrada']
    resposta = cb.central(entrada)
    return render_template('index.html',resposta=resposta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)