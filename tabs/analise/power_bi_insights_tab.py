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
                Recessões econômicas, por outro lado, geralmente resultam em quedas nos preços do petróleo. Durante uma recessão, a demanda por petróleo tende a diminuir devido à desaceleração da atividade econômica. A crise financeira global de 2008 é um exemplo marcante, onde a redução da demanda levou a uma queda acentuada nos preços do petróleo. Similarmente, a crise da dívida europeia que começou em 2010 teve um impacto significativo ao reduzir a demanda de petróleo na região.\n
                 
              
            st.image("assets/img/Eventos_02.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")
                

                :three: **2020 (Colapso para 9 USD):**\n
                Avanços tecnológicos na extração de petróleo, como a exploração de xisto nos Estados Unidos, têm o potencial de aumentar a oferta de petróleo, influenciando os preços. A revolução do xisto na última década fez com que os EUA se tornassem um dos maiores produtores de petróleo, impactando significativamente os preços globais. O desenvolvimento de técnicas de fraturamento hidráulico e perfuração horizontal foram fatores chave nessa transformação.\n
               
            st.image("assets/img/Eventos_03.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")
                
                :four: **2022 (Pico de 133 USD):**\n
                Políticas governamentais e acordos internacionais visando a redução das emissões de carbono podem impactar a demanda por petróleo. A transição para fontes de energia renovável, incentivada por políticas ambientais rigorosas, pode reduzir a dependência de petróleo, afetando os preços a longo prazo. Iniciativas como o Acordo de Paris têm influenciado as políticas energéticas de diversos países, promovendo uma transição para energias mais limpas.\n
                
                st.image("assets/img/Eventos_04.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")
               
                :five: **2023-2024 (Estabilização em torno de 70-80 USD):**\n
                Eventos inesperados, como a pandemia de COVID-19, também têm efeitos substanciais no mercado de petróleo. Em 2020, as restrições de mobilidade e a desaceleração econômica global causadas pela pandemia levaram a uma queda histórica na demanda por petróleo, resultando em preços negativos pela primeira vez na história. Isso evidenciou a vulnerabilidade do mercado a choques de demanda repentinos e extremos.
              
                st.image("assets/img/Eventos_05.png", caption="Análise dos Eventos-Chave 2011-2014 que Impactaram os Preços do Petróleo Brent (Power BI)")
                
                """
            )

            st.image("assets/img/Eventos_02_PBI.jpeg", caption="Gráfico evidenciando os impactos negativas com a pandemia de COVID-19 (Power BI)")

            st.markdown(
                """
                :six: **Descobertas e Explorações:**\n
                Descobertas de novos campos petrolíferos e a exploração em áreas anteriormente inacessíveis, como o Ártico, podem aumentar a oferta de petróleo. Tais descobertas podem estabilizar ou até reduzir os preços, dependendo da magnitude das reservas encontradas e da viabilidade econômica da exploração. A exploração no Ártico e no offshore profundo são exemplos de áreas que estão sendo cada vez mais investigadas.\n
                :seven: **Crise da Dívida Europeia:**\n
                A crise da dívida europeia, iniciada em 2010, teve um impacto significativo no mercado de petróleo. A incerteza econômica e as medidas de austeridade implementadas em vários países europeus levaram a uma diminuição da demanda por petróleo na região, contribuindo para a volatilidade dos preços. Esse período destacou a interconectividade das economias globais e seus efeitos sobre os mercados de commodities.
                """
            )

            st.image("assets/img/Eventos_03_PBI.jpeg", caption="Queda significativa no mercado de petróleo com a crise da dívida europeia (Power BI)")

            st.markdown(
                """    
                :eight: **Colapso do Lehman Brothers:**\n
                O colapso do Lehman Brothers em 2008 marcou o início de uma profunda crise financeira global. Esse evento levou a uma retração severa na economia mundial, resultando em uma queda acentuada na demanda por petróleo e uma subsequente queda nos preços. O impacto desse colapso demonstrou como eventos financeiros podem rapidamente se espalhar e afetar mercados aparentemente não relacionados, como o de petróleo.
                """
            )

            st.image("assets/img/Eventos_04_PBI.jpeg", caption="Profunda crise financeira global com o colapso do Lehman Brothers em 2008 (Power BI)")

            st.subheader(":orange[Análises de Especialistas]")

            st.markdown(
                """   
                Analistas do mercado de petróleo frequentemente monitoram uma combinação de fatores para fazer previsões sobre os preços. Estes incluem relatórios de produção da OPEP, estoques de petróleo dos EUA, dados de consumo energético global e indicadores econômicos gerais. A integração de análises quantitativas e qualitativas é crucial para formar uma visão holística dos possíveis movimentos de preços.
                """
            )

            st.subheader(":orange[Importância da Análise de Eventos]")

            st.markdown(
                """  
                Identificar e entender esses eventos é crucial para prever movimentos futuros nos preços do petróleo. Investidores, governos e empresas de energia dependem dessas análises para tomar decisões informadas, gerenciar riscos e formular estratégias de longo prazo. O monitoramento contínuo e a análise detalhada dos eventos e seus impactos permitem uma resposta proativa às mudanças do mercado, contribuindo para a estabilidade econômica e a segurança energética.
                """
            )
