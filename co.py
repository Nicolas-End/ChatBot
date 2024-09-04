import cohere 
import json
#arquivo para abrir o chatbot final no caso o cohere
co = cohere.Client(api_key="xgpLCWves1QSYw7GB4mrP7MQIWZqaPZnjvoXTwPM")
class ChatBot:
    def __init__(self):
        self.chat_history =[]
        with open('Dados.json', 'r') as dc:
            self.dados = json.load(dc)
    def resposta_cohere(self,pergunta):
        pergunta = pergunta+" Reposta com o maximo de 3 linhas"
        response = co.chat(
            model = "command-r-plus",
            message= pergunta,
            chat_history=self.chat_history,
            documents=self.dados
        )
        self.chat_history = response.chat_history
        return response.text
