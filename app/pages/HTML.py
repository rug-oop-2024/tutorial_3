
import streamlit as st
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
from sklearn.datasets import fetch_openml


# HTML showcase

def app():
    st.title('HTML')
    st.write('This is a simple demo of HTML in Streamlit framework.')
    st.write('You can use the sidebar to navigate through the app.')
    st.write('Have fun!')

    # Add a HTML
    st.markdown('## HTML')
    st.markdown('<h1 style="color:blue;">This is a blue heading</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:red;">This is a red paragraph</p>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.streamlit.io/">This is a link</a>', unsafe_allow_html=True)

    # Showcase pygwalker
    st.markdown('## Pygwalker')
    st.markdown('### Pygwalker is a simple Python package that allows you to create a walking animation of a text.')
    st.markdown('### To install pygwalker, use the following command:')
    st.code('pip install pygwalker')
    st.markdown('### To use pygwalker, use the following code:')
    
    # now lets integrate pygwalker
    data = fetch_openml(name="adult", version=1, parser="auto")
    df = pd.DataFrame(
        data.data,
        columns=data.feature_names,
    )
    st.write(df.head())
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
            


app()