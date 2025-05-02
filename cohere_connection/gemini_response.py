import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
with open('cohere_connection/ChatBot_Presets.json', 'r') as presets_from_json:
        presets = json.load(presets_from_json)
        
context = "\n".join([f"{item['title']}: {item['snippet']}" for item in presets])        
        
        


# Criando o modelo



class ChatBot:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        # Criando o modelo
        self.model = genai.GenerativeModel('gemini-1.5-pro')

        # Criando uma conversa com contexto
        self.chat = self.model.start_chat(history=[])
        
    def ResponseFromGemini(self,question_from_user):
        mensage = f"{context} \n\n{question_from_user}"
        
        response_gemini = self.chat.send_message(mensage)
        
        return response_gemini.text
        
        
