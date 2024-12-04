import streamlit as st
from tabs.tab import TabInterface


class PowerBIInsightsTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Eventos-Chave e Insights Analisados com Power BI]", divider="orange")

            st.markdown(
                """
                Eventos específicos influenciam os preços do petróleo de maneiras distintas. Por exemplo, interrupções na produção frequentemente resultam em alta nos preços, enquanto períodos de recessão econômica tendem a provocar reduções. Reconhecer e compreender esses fatores é essencial para antecipar as variações futuras nos preços.
                """
            )
            st.image("assets/img/Evolucao_preco.png", caption="Gráfico de Insights e Eventos-Chave: Análise de Preços (Power BI)")

            st.subheader(":orange[Análise Detalhada dos Eventos e Seus Impactos]")
            st.markdown(
                """
                A compreensão dos eventos que impactam o mercado de petróleo é essencial para prever flutuações nos preços. Eventos específicos podem ter impactos significativos e variados nos preços do petróleo, influenciando diretamente a oferta e a demanda.\n
                :one: **2011-2014 (Preços elevados, acima de 100 USD):**\n
                A alta foi impulsionada pela instabilidade política no Oriente Médio e Norte da África, decorrente da Primavera Árabe (2011).Sanções econômicas contra o Irã restringiram a oferta de petróleo no mercado global.O crescimento econômico global pós-crise de 2008 também sustentou uma forte demanda.\n
                """
            )

            st.image("assets/img/Eventos_01.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")

            st.markdown(
                """    
                :two: **2014-2016 (Queda acentuada, de 115 USD para 26 USD):**\n
                A queda abrupta foi causada por uma estratégia da OPEP de manter alta a produção de petróleo, tentando proteger sua participação no mercado frente ao aumento da produção de petróleo de xisto nos EUA.A desaceleração econômica da China também reduziu a demanda global, ampliando o excesso de oferta.\n
              """
            )     
              
            st.image("assets/img/Eventos_02.png", caption="Análise dos Eventos-Chave 2014-2016 que Impactaram os Preços do Petróleo Brent (Power BI)")
         
        st.markdown(
                """      
                :three: **2020 (Colapso para 9 USD):**\n
                A pandemia de COVID-19 provocou um choque de demanda devido à redução drástica de viagens e atividades industriais.Em abril de 2020, uma guerra de preços entre Arábia Saudita e Rússia contribuiu para intensificar a queda, resultando até em preços negativos nos contratos futuros (não representados diretamente no gráfico).\n
                 """
            )   
           
        st.image("assets/img/Eventos_03.png", caption="Análise dos Eventos-Chave 2020 que Impactaram os Preços do Petróleo Brent (Power BI)")

            st.markdown(
                """    
               :four: **2022 (Pico de 133 USD):**\n
                A invasão da Ucrânia pela Rússia gerou temores de interrupções no fornecimento global, uma vez que a Rússia é um dos maiores exportadores de petróleo.Sanções contra o setor energético russo agravaram a incerteza no mercado, impulsionando os preços.\n
                 """
            )   
                
                
            
                
