
import streamlit as st

# Show case user input

def app():
    st.title('User Input')
    st.write('This is a simple demo of user input in Streamlit framework.')
    st.write('You can use the sidebar to navigate through the app.')
    st.write('Have fun!')

    # Add a text input to the app
    first_name = st.text_input('Enter your first name', 'John')
    st.write('Your first name is:', first_name)

    # Add a number input to the app
    age = st.number_input('Enter your age', 18, 100, 25)
    st.write('Your age is:', age)

    # Add a slider to the app
    weight = st.slider('Enter your weight', 40, 150, 70)
    st.write('Your weight is:', weight)

    # Add a select
    status = st.selectbox('Select your status', ['Single', 'Married', 'Divorced'])

    # Add a multiselect
    colors = st.multiselect('Select your favorite colors', ['Red', 'Green', 'Blue'])

    # Add a file uploader
    uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

    # Add a date input
    date = st.date_input('Enter a date')

    # Add a time input
    time = st.time_input('Enter a time')

    # Add a color picker
    color = st.color_picker('Pick a color', '#00f900')

    # Add a text area
    description = st.text_area('Enter a description', 'Description goes here')
    st.write('Your description is:', description)

    # Add a markdown
    st.markdown('## Markdown')
    st.markdown('**This** is a markdown')

    # Add a code block
    st.code('import pandas as pd\nimport numpy as np')

    # Add a JSON
    st.json({'name': 'John', 'age': 25})

    # Add a progress bar
    import time

    'Starting a long computation...'
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

    # Add a placeholder
    placeholder = st.empty()
    placeholder.text('This is a placeholder')

    # Add a button
    if st.button('Click me'):
        st.write('You clicked the button!')

    # Add a checkbox
    if st.checkbox('Check me out'):
        st.write('You checked the box!')

    # Add a radio button
    radio = st.radio('Radio', ['Option 1', 'Option 2'])
    st.write('You selected:', radio)

    # Add a sidebar
    st.sidebar.title('Sidebar')
    st.sidebar.write('This is a sidebar')
    st.sidebar.write('You can use it to navigate through the app')

    # Add a file downloader
    st.markdown('## File Downloader')
    st.markdown('Click the button below to download a file')
    st.markdown('This is a dummy file')
    st.markdown('Download [dummy.txt](https://www.google.com)')

    # Add a link
    st.markdown('## Link')
    st.markdown('Click the link below to visit Google')
    st.markdown('[Google](https://www.google.com)')

    # Add a video
    st.markdown('## Video')
    st.markdown('Watch the video below')
    st.header("Chopin's Prelude (introduction) in E Minor")
    st.video('https://www.youtube.com/watch?v=BgQmSVE60XE')


app()