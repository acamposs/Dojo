import pandas as pd
import numpy as np

#criar uma matriz aleatória 3 x 4 usando numpy
matriz_aleatoria = np.random.rand (3, 4)
print(matriz_aleatoria)

#criando tabela de frutas da lista de compras contendo o nome e a quantidade
listaCompras = ['banana', 'pera']
quantLista = [2,2]
dadosLista = {'fruta':listaCompras, 'quantidade':quantLista}
listaCompras = pd.DataFrame(dadosLista)
listaCompras.to_csv ('lista.csv')

#criando tabela de frutas da feira contendo o nome e a quantidade
fruta = ['banana','maça','pera','abacaxi']
quantidade = [3,7,2,8]
dados = {'fruta':fruta, 'quantidade':quantidade}
feira = pd.DataFrame(dados)
feira.to_csv('feira.csv')

# Carrega os dados das listas
listaCompras = pd.read_csv('lista.csv')
feira = pd.read_csv('feira.csv')

# Junta as duas tabelas com base no nome da fruta
listaCompras = pd.merge(listaCompras, feira, on='fruta')

# Calcula a quantidade de cada fruta restante na feira
listaCompras['quantidade_restante'] = listaCompras['quantidade_y'] - listaCompras['quantidade_x']

# Seleciona apenas as colunas relevantes
listaCompras = listaCompras[['fruta', 'quantidade_restante']]

# Exibe a lista de compras personalizada
print('Restará na feira a seguinte quantidade de frutas:\n', listaCompras)