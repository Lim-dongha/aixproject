import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('./data/mydata.csv')

# global variable
url = 'https://youtu.be/XyEOEBsa8I4?si=4KP2Uj6KhS9hHIP3'

# dictionary
urls = {
    '윤리': ['1', '2'],
    '코딩': ['3', '4']
}

st.title('This is my first webapp!!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(url)

    with st.expander('SubContent2...'):
        st.subheader('ImageContent1...')
        st.image('./images/1.jpg')
        st.image('./images/2.jpg')   
        st.image('./images/3.jpg')   
        st.image('./images/4.jpg')

    with st.expander('SubContent3...'):
        st.subheader('HTMLContent1...')
        import streamlit.components.v1 as htmlviewer           
        with open('./htmls/index.html','r', encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height=800)

    with st.expander('SubContent4...'):
        st.subheader('DataAppContent1...')
        st.table(df)
        st.write(df.describe())
        fig, ax = plt.subplots(figsize=(20,10))
        df.plot(ax=ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png')

with col2:
    with st.expander('Tips...'):
        st.info('Tips........')

