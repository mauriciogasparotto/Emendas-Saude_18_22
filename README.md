# Emendas parlamentares para Ministério da Saúde - 2018 a 2022

## O projeto:

Analisar os valores liberados por verbas parlamentares ao Ministério da Saúde entre os anos de 2018 e 2022. Os valores estão divididos nas categorias **Valores Empenhados**, **Valores Pagos** e **Valores Liquidados**, para verificar se o dinheiro foi totalmente gasto, ou se houve restos não utilizados.

O período se deve pelo fato de que, no início de 2020, a Organização Mundial da Saúde decretou pandemia mundial devido à Covid-19. O evento serve de parâmetro para avaliar os gastos com o Ministério da Saúde pré e pós-pandemia.

Os dados foram extraídos do Portal da Transparência - detalhamento de emendas parlamentares. Os dados podem ser acessados por este [link](https://portaldatransparencia.gov.br/emendas/consulta?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=codigoEmenda%2Cano%2CtipoEmenda%2Cautor%2CnumeroEmenda%2ClocalidadeDoGasto%2Cfuncao%2Csubfuncao%2CvalorEmpenhado%2CvalorLiquidado%2CvalorPago%2CvalorRestoInscrito%2CvalorRestoCancelado%2CvalorRestoPago).

## Objetivo:

Será que os houve relevante aumento de verbas para o MS em virtude da pandemia? Os valores empenhados realmente foram utilizados em sua totalidade? Houve alguma interferência ideológica/política na destinação das verbas?

## Estrutura do repositório:

* **data:** arquivos **.csv** baixados no site do Portal da Transparência;
* **img:** capturas de tela e gráficos do projeto;
* **code:** estrutura dos códigos para **Jupyter Notebook** (.ipynb) e **VSCode** (.py);
* **english version:** a translate of **readme.md** (.pdf).

## Linguagem utilizada:

* **Python**

## Bibliotecas:

* **Pandas**
* **Numpy**
* **Matplotlib**

## Metodologia:

Após baixar o arquivo no formato **.csv**, os dados foram tratados com **Pandas** para visualização do dataset. Em seguida, foram feitos os devidos filtros pelo período de 2018 e 2022, bem como das colunas de interesse (Valor Empenhado, Valor Liquidado e Valor Pago. A biblioteca **Numpy** permitiu criar np.arange, np.array e np.sum para sequenciar e tratar os valores para cada barra do gráfico.

<img src="/img/dataset.png">

###
Após somar os valores das emendas por ano e por critério, passou a plotagem do gráfico em **Matplotlib**. O modelo escolhido foi o barras horizontais agrupadas, uma vez que os valores são altos e incluir os rótulos tornariam mais legíveis. Outros modelos foram testados, mas mostraram-se pouco legíveis (colunas verticais agrupadas, por exemplo). E, também, os rótulos dos valores foram encurtados, devido aos mesmos serem extensos para leitura.

<img src="/img/grafico.png">

###
## Considerações:

O gráfico mostra claramente o expressivo aumento das verbas destinadas à Saúde já no ano de 2020 (os primeiros casos mundiais de Covid-19 ocorreram no final de 2019; a pandemia foi declarada no início de 2020).

Os valores empenhados saltaram de 6,86 bilhões de reais (2019) para 12,7 bilhões (2020). No ano seguinte, 15,8 bilhões.

Entretanto, também há uma clara diferença quando se analisam os Valores Empenhados x Valores Pagos. Enquanto em 2019 esta diferença era de cerca de 1 bilhão, em 2020 a diferença ficou em pouco mais de 3 bilhões (mesma diferença pode ser notada em 2021).

Em 2022 a diferença volta a pouco mais de 1 bilhão (14,87 em valores empenhados contra 13,4 bilhões em valores pagos).

**OBS**: o dataset permite, ainda, que sejam realizadas pesquisas pelo nome do autor, âmbito da aplicação da verba (nacional ou regional) e ainda traz a identificação do Estado/município do autor e aplicação da emenda, o que pode ampliar os dados para novas abordagens.

### Entretanto....

Mas, olhar friamente apenas os números pode levar a conclusões precipitadas. Deve-se analisar o contexto em que estas verbas foram destinadas.

Durante todo o período da pandemia, vários casos de desvio de dinheiro, superfaturamento, corrupção e destinação indevida foram relatados e ainda hoje (2023) estão sendo investigados pelos órgãos policiais.

Acrescente-se, também, que houve uma CPI pelo Senado da República - a CPI da Pandemia - que investigou e demonstrou casos de corrupção e desvio de dinheiro público.
