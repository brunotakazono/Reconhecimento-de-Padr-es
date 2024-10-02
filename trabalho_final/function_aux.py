import numpy as np
import pandas as pd

def calcular_media_individual_por_chave(dict):
    medias_por_chave = {}
    std_por_chave = {}

    dict_chaves = {}
    for chave, valores in dict.items():
        media = np.mean(valores)
        std = np.std(valores)
        dict_chaves[f'{chave}_media'] = media
        dict_chaves[f'{chave}_std'] = std


    df = pd.DataFrame([dict_chaves])
    return df

def format_dict(d):
    return str(d).replace('{', '').replace('}', '').replace("'", '')

def format_list(l):
    return ', '.join(l)



