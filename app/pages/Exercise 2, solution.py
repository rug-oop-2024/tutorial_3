
from pathlib import Path

from data_plotter.data_handler import Dataset
from data_plotter.data_plotter import DataPlotter
from glob import glob
import matplotlib.pyplot as plt

import streamlit as st

options = glob("**/*.csv", recursive=True)

path = st.selectbox("Select a dataset", options)

if path:
    data_path = Path(path)

    dataset = Dataset(data_path)
    plotter = DataPlotter(dataset)
    df = dataset.data
    st.write(df.head())

    # Choose columns to plot
    columns = st.multiselect("Select columns to plot", dataset.columns)
    fig = None
    print(columns)
    if len(columns) == 0:
        st.write("Please select at least one column to plot.")
    if len(columns) == 1:
        fig = plotter.hist_1d(columns[0])
    if len(columns) == 2:
        fig = plotter.scatter_2d(columns[0], columns[1])
    if len(columns) == 3:
        fig = plotter.scatter_3d(columns[0], columns[1], columns[2])
    if len(columns) > 3:
        st.error("Please select at most 3 columns to plot.")
    if fig:
        st.pyplot(fig)

