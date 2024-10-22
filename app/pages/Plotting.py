
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

    # Now for a black hole
    # Black Hole Simulation
    st.markdown('## Black Hole Simulation')

    # Create a grid for black hole simulation
    # Constants
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    c = 299792458     # speed of light in m/s
    M = 10 * 1.989e30  # mass of the black hole (10 solar masses)
    r = np.linspace(0.1, 15, 400)  # Avoid division by zero
    theta = np.linspace(0, 2 * np.pi, 400)
    R, Theta = np.meshgrid(r, theta)

    # Calculate the gravitational potential around a black hole (realistic)
    V = -G * M / (R * c**2)  # Gravitational potential per unit mass

    # Convert polar coordinates to Cartesian coordinates for 3D plotting
    X_bh = R * np.cos(Theta)
    Y_bh = R * np.sin(Theta)

    # Create a 3D surface plot for the black hole gravitational potential
    fig_bh = plt.figure(figsize=(10, 8))
    ax_bh = fig_bh.add_subplot(111, projection='3d')

    # Plotting the surface
    surface_bh = ax_bh.plot_surface(X_bh, Y_bh, V, cmap='inferno', edgecolor='none')

    # Adding labels and title
    ax_bh.set_title('Gravitational Potential around a Black Hole', fontsize=12)
    ax_bh.set_xlabel('X-axis')
    ax_bh.set_ylabel('Y-axis')
    ax_bh.set_zlabel('Gravitational Potential')

    # Add color bar for scale
    fig_bh.colorbar(surface_bh, ax=ax_bh, shrink=0.5, aspect=5, label='Potential (simulated)')

    # Display the black hole simulation plot in Streamlit
    st.pyplot(fig_bh)


app()
  