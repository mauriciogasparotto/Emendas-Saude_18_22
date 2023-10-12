# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Leitura do arquivo CSV com os dados das emendas (Portal da Transparência)
emendas = pd.read_csv(r'Emendas.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip', decimal=',')


# Filtro dos dados de emendas para o período de 2018 a 2022 e para a função "Saúde"
emendas_saude = emendas[(emendas['Ano da Emenda'] >= 2018) & (emendas['Ano da Emenda'] <= 2022) & (emendas['Nome Função'] == 'Saúde')]


# Agrupa os dados por ano e soma os valores das colunas monetárias
emendas_saude_sum = emendas_saude.groupby('Ano da Emenda')[['Valor Empenhado', 'Valor Liquidado', 'Valor Pago']].sum()


# Configuração para plotagem do gráfico:

# Dimensões
fig, ax = plt.subplots(figsize=(9, 6))

# Definir a largura das colunas
bar_height = 0.25

# Definir a sequência de valores para cada coluna
r1 = np.arange(len(emendas_saude_sum.index))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]

# Definir das colunas e cores correspondentes
columns = ['Valor Empenhado', 'Valor Pago', 'Valor Liquidado']
colors = [0, 1, 2]

# Plotagem das barras para cada coluna
for i, column in enumerate(columns):
    plt.barh(r1 + i * bar_height, emendas_saude_sum[column].values, color=plt.cm.Set2(colors[i]), height=bar_height, edgecolor='white', label=column)

# Adicionar os valores nas barras com formatação compacta e afasta os rótulos
for i, column in enumerate(columns):
    for j, value in enumerate(emendas_saude_sum[column]):
        formatted_value = 'R$ {:,.2f}'.format(value / 1000000000)  # Formatando para bilhões com três casas decimais
        plt.text(value + 0.5, r1[j] + i * bar_height, formatted_value, ha='left', va='center', fontsize=11, fontweight='normal', fontfamily='Arial')

# Adicionar o título do gráfico
plt.title('Emendas parlamentares para Saúde de 2018 a 2022', fontsize=16, fontweight='normal', fontfamily='Arial')

# Adicionar os rótulos dos eixos x e y com fonte e tamanho configurados
plt.ylabel('Ano da Emenda', fontsize=14, fontweight='normal', fontfamily='Arial')
plt.xlabel('Valor (em bilhões de reais)', fontsize=14, fontweight='normal', fontfamily='Arial')
plt.yticks(fontsize=12, fontfamily='Arial')  # Configura fonte e tamanho dos rótulos do eixo y

# Definir as posições e labels do eixo y
plt.yticks([r + bar_height for r in range(len(emendas_saude_sum.index))], emendas_saude_sum.index)

# Inverter o eixo y
plt.gca().invert_yaxis()

# Excluir os valores da escala do eixo X (opcional)
plt.xticks([])

# Excluir a linha de quadro do gráfico (opcional)
plt.box(False)

# Adicionar a legenda
plt.legend(loc='upper right', bbox_to_anchor=(1.02, 1))

# Adicionar o crédito para a fonte dos dados no canto inferior direito
source_credit = "Fonte dos dados: Portal da Transparência"
plt.text(0.95, 0.02, source_credit, transform=fig.transFigure, fontsize=8, ha='right', va='bottom', fontfamily='Arial')

# Plotar o gráfico
plt.show()
