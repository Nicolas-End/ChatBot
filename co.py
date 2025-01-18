import cohere 
#arquivo para abrir o chatbot final no caso o cohere
co = cohere.Client(api_key="")
class ChatBot:
    def __init__(self):
        self.chat_history =[]

    def resposta_cohere(self,pergunta,dados):
        pergunta = pergunta+" Reposta com o maximo de 4 linhas"
        response = co.chat(
            model = "command-r-plus",
            message= pergunta,
            chat_history=self.chat_history,
            documents=dados
        )
        self.chat_history = response.chat_history
        return response.text
