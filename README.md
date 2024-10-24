# Tutorial 3 code

In this tutorial, we built a Streamlit application for data plotting.

The `data_handler` module provides a `Dataset` class which is a facade over `pandas.DataFrame`.

The `data_plotter` module provides a `DataPlotter` class which takes in a dataset and allows to plot a histogram, a 2d- or a 3d-scatterplot of a select number of variables.

The streamlit app:
* Lets a user read a dataset from a csv file
* Converts the dataset into the `Dataset` class
* Allows the user to select some features from the dataset
* Lets the user produce the desired plot given the features provided
