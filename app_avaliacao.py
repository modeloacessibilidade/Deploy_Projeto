# importando as bibiliotecas
import streamlit as st
import pandas as pd
import numpy as np

import pickle


# Carregando o modelo
model =  pickle.load(open('avaliacao_v2.pkl', 'rb'))


# Criando uma função para receber as features
def predict(review_count,Tu_We_Th_minutos_func, Sunday_minutos_func, Friday_minutos_func ):
    input=np.array([[review_count,Tu_We_Th_minutos_func, Sunday_minutos_func, Friday_minutos_func]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0] [0], 2)
    return float(pred)
    



def main():
    
    # Add titulo, imagem e uma pequena descrição do nosso projeto
    from PIL import Image
    image =  Image.open("stars.png")
    st.image(image, use_column_width=False)
   

    
    st.title('Descubra qual será avaliação do seu estabelecimento')
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">
     Nós te ajudamos a identificar o que é importante para os clientes em um estabelecimento na hora de avaliar.</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.sidebar.subheader('Por favor preencha as informações abaixo e clique no botão para saber qual será a sua avaliação!')

    
    # inserindo os dados para predição
    review_count =  st.sidebar.number_input("Quantidade de avaliações do seu estabalecimento", min_value=3, max_value=10129, value=294)
    Tu_We_Th_minutos_func =  st.sidebar.number_input("Tempo médio de funcionamento de 3° à 5° (Minutos)", min_value=0, value=640, max_value=1440)
    Sunday_minutos_func = st.sidebar.number_input("Tempo de funcionamento aos Domingos ( Minutos)", min_value=0,  value=600, max_value=1440)
    Friday_minutos_func =  st.sidebar.number_input("Tempo de funcionamento às Sextas-feiras  (Minutos)", min_value=0, value=660, max_value=1440)
    
    #definindo o nível de cores para o tipo de avaliação
    boa_html="""  
      <div style="background-color:#38ff77;padding:40px >
       <h2 style="color:green;text-align:center;"> BOA</h2>
       </div>
    """
       
    ruim_html="""  
      <div style="background-color:#d61d40;padding:40px >
       <h2 style="color:red ;text-align:center;">  RUIM</h2>
       </div>
        """
 

     # criando botão para predição
    if st.sidebar.button("Clique para fazer a avaliação!"):
        output=predict(review_count,Tu_We_Th_minutos_func, Sunday_minutos_func, Friday_minutos_func)
        st.success('De acordo com as informações fornecidas sua avaliação será:')
        
        if output > 0.5:
             st.markdown(ruim_html,unsafe_allow_html=True)
        else:
            st.markdown(boa_html,unsafe_allow_html=True)
        st.write('A probabilidade de ocorrer Uma avaliação ruim é:')
        st.write(output)
    

            

if __name__ == '__main__':
    main()           