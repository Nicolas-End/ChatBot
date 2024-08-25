
import pandas as pd
import random
try :
    df_perguntas = pd.read_excel("Perguntas.xlsx",engine = 'openpyxl')
    df_respostas = pd.read_excel("Respostas.xlsx",engine = 'openpyxl')
except FileNotFoundError:
    print("Deu Erro")
#importando bibliotecas necessarias
import pandas as pd
import random
import co
#lendo a base de dados principal
try :
    df_perguntas = pd.read_excel("Perguntas.xlsx",engine = 'openpyxl')
    df_respostas = pd.read_excel("Respostas.xlsx",engine = 'openpyxl')

except FileNotFoundError:
    print("Deu Erro")
#organizando o chatbot
def central(usuario):
    valor = ''
    if saudar(usuario) != None:
        valor = saudar(usuario)
        return valor
    elif Comprimentar(usuario) != None:
        valor = Comprimentar(usuario)
        return valor
    #caso a pergunta n esteja na base de dados ele acessara o cohere
    else:
        return co.resposta_cohere(usuario)


def saudar (usuario):
    if usuario.lower() in df_perguntas['Saudações'].str.lower().tolist():
        return(random.choice(df_respostas['Saudações']))
def Comprimentar(usuario):
    if usuario.lower() in df_perguntas['Comprimentar'].str.lower().tolist():
        return(random.choice(df_respostas['Comprimentar']))

