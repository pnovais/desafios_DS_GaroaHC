'''
Solucao dada ao problema enem-1 do codenation
'''

import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
df = df.set_index('NU_INSCRICAO')

pesos_notas = {
        'NU_NOTA_MT': 3,
        'NU_NOTA_CN': 2,
        'NU_NOTA_CH': 1,
        'NU_NOTA_LC': 1.5,
        'NU_NOTA_REDACAO': 3,
    }

res = sum(
	w*df[col] for col,w in pesos_notas.items()
	)/sum(pesos_notas.values())
res.name = 'NOTA_FINAL'
res.sort_values(ascending=False).head(20).to_csv('answer.csv',header=True)

