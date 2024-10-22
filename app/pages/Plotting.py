
import streamlit as st
from sklearn.datasets import fetch_openml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = fetch_openml(name="adult", version=1, parser="auto")
df = pd.DataFrame(
    data.data,
    columns=data.feature_names,
)


# Streamlit showcase of charting, use numpy functions, and , build up with simple fake data, dont use pygwalker

def app():
    st.title('Plotting')
    st.write('This is a simple demo of plotting in Streamlit framework.')
    st.write('You can use the sidebar to navigate through the app.')
    st.write('Have fun!')

    # Add a plot
    st.markdown('## Plot')
    st.markdown('### Line Chart')
    st.line_chart(np.random.randn(20, 2))

    st.markdown('### Area Chart')
    st.area_chart(np.random.randn(20, 2))

    st.markdown('### Bar Chart')
    st.bar_chart(np.random.randn(20, 2))

    # Add a plot
    st.markdown('## DataFrame')
    st.write(df.head())

    # Funny plots
    # Einstein field equations
    st.markdown('## Einstein Field Equations')
    st.latex(r'''
        G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
    ''')

    # Plot example
    # Create a grid of points in 2D
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    # Define a function for a gravitational well, simulating the curvature of spacetime
    Z = -1 / np.sqrt(X**2 + Y**2 + 1)

    # Create a 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the surface
    surface = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')

    # Adding labels and title
    ax.set_title(r'Einstein Field Equations: 3D Gravitational Well', fontsize=12)
    ax.set_xlabel('X-axis (space)')
    ax.set_ylabel('Y-axis (space)')
    ax.set_zlabel('Z-axis (curvature)')

    # Add color bar for scale
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='Curvature (simulated)')

    # Display the plot in Streamlit
    st.pyplot(fig)


app()
  