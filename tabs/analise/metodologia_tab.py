import streamlit as st
from tabs.tab import TabInterface


class MetodologiaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Origem e Análise dos Dados]", divider="orange")

            st.markdown(
                """
                Os dados utilizados nesta análise foram extraídos do site do **[Instituto de Pesquisa Econômica Aplicada (Ipea)](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)**.
                Após a extração, os dados foram salvos em um arquivo **Microsoft Excel**, preparando-os para uma análise detalhada utilizando **Python**.
                """
            )
            st.markdown(
                """
                Para a análise dos dados, foi utilizado o arquivo Excel como fonte. Com a ajuda do Python, foram construídos gráficos que permitem visualizar a variação do preço do petróleo ao longo do tempo e entender as informações que trabalhadas.
                """
            )
            st.subheader(":orange[Aplicando o modelo LSTM]")
            st.markdown(
                """
                Utilizando o mesmo arquivo Excel contendo os dados históricos do preço do petróleo, aplicamos o modelo LSTM (Long Short-Term Memory) para prever os preços futuros. 

                Para avaliar a performance do modelo e determinar a confiabilidade das previsões, calculamos diversas métricas de desempenho, incluindo:

                - Coeficiente de Determinação (R²)
                - Erro Médio Quadrático (MSE)
                - Erro Médio Absoluto (MAE)
                - Erro Percentual Absoluto Médio (MAPE)
                - Raiz do Erro Médio Quadrático (RMSE)

                Essas métricas nos permitem compreender melhor a precisão do modelo e a qualidade das previsões geradas.

                Segundo o site *Análise Macro*, temos as seguintes definições:

                - **R² Score (Coeficiente de Determinação):** O R² Score mede a proporção da variância na variável dependente que é previsível a partir da variável independente. Valores de R² próximos de 1 indicam um ajuste perfeito do modelo aos dados, enquanto valores próximos de 0 indicam um ajuste pobre. No caso de R², quanto mais próximo de 1, melhor.\n
                - **MSE (Erro Quadrático Médio):** O MSE é a média dos quadrados dos erros entre os valores reais e os valores previstos. Ele fornece uma medida da dispersão dos erros. Valores mais baixos de MSE indicam que o modelo tem uma boa capacidade de prever os valores reais.\n
                - **MAE (Erro Médio Absoluto):** O MAE é a média dos valores absolutos dos erros entre os valores reais e os valores previstos. Ele fornece uma medida da magnitude média dos erros do modelo. Valores menores de MAE indicam que o modelo tem uma boa capacidade de prever os valores reais.\n
                - **MAPE (Erro Percentual Absoluto Médio):** O MAPE é a média dos valores absolutos dos erros percentuais entre os valores reais e os valores previstos, expressa como uma porcentagem do valor real. Ele fornece uma medida da precisão percentual média das previsões. Valores menores de MAPE indicam que o modelo tem uma boa precisão em suas previsões.\n
                - **RMSE (Raiz do Erro Quadrático Médio):** O RMSE é a raiz quadrada do MSE e fornece uma medida da dispersão dos erros em unidades da variável de interesse. Assim como o MSE, valores mais baixos de RMSE indicam que o modelo tem uma boa capacidade de prever os valores reais.
                """
            )
        
