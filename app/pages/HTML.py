
import streamlit as st
import pygwalker as pyg


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

    # Add a Pygame
    st.markdown('## Pygame')
    st.markdown('This is a Pygame')

    # Add a Pygame
    st.markdown('## Pygame')
    st.markdown('This is a Pygame')