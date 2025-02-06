import cohere 
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv('COHERE_API_KEY')
cohere_api = cohere.Client(api_key=api_key)

#Pega todos os presets do ChatBot
with open('cohere_connection/Presets_to_cohere.json', 'r') as presets_from_json:
        presets = json.load(presets_from_json)

class ChatBot:
    def __init__(self):
        self.chat_history =[]
        self.preset_to_the_response = presets
    #Esta Função Pega a pergunta do usuario 
    #Manda para api do cohere, pega a resposta dela
    def response_from_cohere(self,question_from_user):
        
        #Limita o numero de linhas de resposta da api
        question_from_user = question_from_user+" Reposta com o maximo de 4 linhas"
        
        response = cohere_api.chat(

            model = "command-r-plus",
            message= question_from_user,
            chat_history=self.chat_history,
            documents=self.preset_to_the_response
        )
        self.chat_history = response.chat_history
        return response.text
