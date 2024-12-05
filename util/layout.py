import streamlit as st
from st_pages import show_pages, Page

def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge: Fase 4", ":computer:", use_relative_hash=True),
            Page(
                "./pages/analise.py",
                "Exploração e Insights",
                ":chart_with_upwards_trend:",
                use_relative_hash=True,
            ),

              #Page(
              #  "./pages/deploy.py",
             #   "Deploy",
             #   ":gear:",
              #  use_relative_hash=True,
           # ),

            Page(
                "./pages/conclusao.py",
                "Conclusão",
                ":white_check_mark:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/referencias.py",
                "Referências",
                ":page_facing_up:",
                use_relative_hash=True,
            ),
        ]
    )
    
    with st.sidebar:
        st.subheader("Grupo")
        st.text("Edson Yuji Murata") 
        st.text("Lucas David de Oliveira")
        st.text("Rafael Ishiy Macedo") 
        st.text("Raphaela Rodrigues Coelho")
        
        st.divider()
        
        st.subheader("Guia de Instalação e Execução do Aplicativo Localmente")

        # Passo 1: Criação e ativação do ambiente virtual
        st.markdown("**1º** Crie e ative um ambiente virtual:")

        # Criação do ambiente virtual
        st.code("python -m venv venv", language="shell")

        # Ativação do ambiente virtual para Linux
        st.markdown("Para Linux, use:")
        st.code("source venv/bin/activate", language="shell")

        # Ativação do ambiente virtual para Windows
        st.markdown("Para Windows, use:")
        st.code("venv\\Scripts\\activate", language="shell")

        # Passo 2: Instalação das dependências
        st.markdown("**2º** Instale as bibliotecas com as versões corretas:")
        st.code("pip install -r requirements.txt", language="shell")

        # Passo 3: Execução do aplicativo
        st.markdown("**3º** Execute o aplicativo:")
        st.code("streamlit run main.py", language="shell")



        
  
