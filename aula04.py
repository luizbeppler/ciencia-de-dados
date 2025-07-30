import numpy as np
from scipy import stats

# Nota de matemática
notas = [78, 85, 91, 73, 88, 92, 79, 85, 90, 87]



# Calcular a média
media = np.mean(notas)
print(f'Média: {media}')



# Calcular a moda
moda = stats.mode(notas, keepdims=True)
print(f'Moda: {moda.mode[0]}, Frequência: {moda.count[0]}')


# Conjunto de dados exemplo
dados = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]

# Calcular quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

# Calcular decis
decis = np.percentile(dados, [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f'Decis: {decis}')

# Calcular percentis
percentis = np.percentile(dados, [10, 25, 50, 75, 90])
print(f'Percentis: {percentis}')
