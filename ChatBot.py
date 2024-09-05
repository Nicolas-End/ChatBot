#importando bibliotecas necessarias
import co
chatbot=co.ChatBot()

#organizando o chatbot
def central(usuario):
    return chatbot.resposta_cohere(pergunta=usuario)


