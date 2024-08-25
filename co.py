import cohere 

#arquivo para abrir o chatbot final no caso o cohere
co = cohere.Client(api_key="xgpLCWves1QSYw7GB4mrP7MQIWZqaPZnjvoXTwPM")
def resposta_cohere(pergunta):
    response = co.chat(
        model = "command-r-plus",
        message= pergunta,

    )
    return response.text
