import cohere 
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('YOUR_COHERE_API_KEY')
cohere_api = cohere.Client(api_key=api_key)

class ChatBot:
    def __init__(self):
        self.chat_history =[]
    
    #Esta Função Pega a pergunta do usuario 
    #Manda para api do cohere, pega a resposta dela
    def response_from_cohere(self,question_from_user,datas):
        
        #Limita o numero de linhas de resposta da api
        question_from_user = question_from_user+" Reposta com o maximo de 4 linhas"
        
        response = cohere_api.chat(

            model = "command-r-plus",
            message= question_from_user,
            chat_history=self.chat_history,
            documents=datas
        )
        self.chat_history = response.chat_history
        return response.text
