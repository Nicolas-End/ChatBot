
import pandas as pd
import random
try :
    df_perguntas = pd.read_excel("Perguntas.xlsx",engine = 'openpyxl')
    df_respostas = pd.read_excel("Respostas.xlsx",engine = 'openpyxl')
except FileNotFoundError:
    print("Deu Erro")
def central(usuario):
    valor = ''
    if saudar(usuario) != None:
        valor = saudar(usuario)
        return valor
    elif Comprimentar(usuario) != None:
        valor = Comprimentar(usuario)
        return valor
    else:
        return "Não encotrado"

def saudar (usuario):
    if usuario.lower() in df_perguntas['Saudações'].str.lower().tolist():
        return(random.choice(df_respostas['Saudações']))
def Comprimentar(usuario):
    if usuario.lower() in df_perguntas['Comprimentar'].str.lower().tolist():
        return(random.choice(df_respostas['Comprimentar']))

