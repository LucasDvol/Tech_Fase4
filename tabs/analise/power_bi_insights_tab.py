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
                :one: **2011-2014 (Preços elevados, acima de 100 USD):**\n
                - A alta foi impulsionada pela instabilidade política no Oriente Médio e Norte da África, decorrente da Primavera Árabe (2011).
                - Sanções econômicas contra o Irã restringiram a oferta de petróleo no mercado global.
                - O crescimento econômico global pós-crise de 2008 também sustentou uma forte demanda.
                """
            )
            st.image("assets/img/Eventos_01.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")

            st.markdown(
                """
                :two: **2014-2016 (Queda acentuada, de 115 USD para 26 USD):**\n
                - A queda abrupta foi causada por uma estratégia da OPEP de manter alta a produção de petróleo.
                - A desaceleração econômica da China também reduziu a demanda global, ampliando o excesso de oferta.
                """
            )
            st.image("assets/img/Eventos_02.png", caption="Análise dos Eventos-Chave 2014-2016 que Impactaram os Preços do Petróleo Brent (Power BI)")

            st.markdown(
                """
                :three: **2020 (Colapso para 9 USD):**\n
                - A pandemia de COVID-19 provocou um choque de demanda devido à redução drástica de viagens e atividades industriais.
                - Em abril de 2020, uma guerra de preços entre Arábia Saudita e Rússia intensificou a queda, resultando até em preços negativos nos contratos futuros.
                """
            )
            st.image("assets/img/Eventos_03.png", caption="Análise dos Eventos-Chave 2020 que Impactaram os Preços do Petróleo Brent (Power BI)")
