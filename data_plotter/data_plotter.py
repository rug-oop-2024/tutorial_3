import numpy as np

from matplotlib import pyplot as plt

from data_plotter.data_handler import Dataset

class DataPlotter:
    '''
    A class to plot instances of the Dataset class
    '''
    def __init__(
            self,
            data: Dataset,
        ) -> None:
        self._data = data

    def hist_1d(self, variable: str, **kwargs) -> plt.Figure:
        '''
        Plots a 1D histogram of the dataset for the given variable

        Arguments:
        variable (str): The variable to plot
        **kwargs: Arbitrary keyword arguments for plt.hist

        Returns:
        None
        '''
        data = self._data[variable]

        if "bins" not in kwargs:
            kwargs["bins"] = 20

        plt.hist(data, **kwargs)
        plt.xlabel(variable)
        plt.ylabel("Frequency")
        plt.title(f"{variable} histogram")
        plt.show()
        return plt.gcf()

    def scatter_2d(self, x_variable: str, y_variable: str, **kwargs) -> plt.Figure:
        '''
        Plots a 2D scatter plot of the dataset for the given
        x and y variables.

        Arguments:
        x_variable (str): The x variable to plot
        y_variable (str): The y variable to plot
        **kwargs: Arbitrary keyword arguments for plt.scatter

        Returns:
        None
        '''
        data = self._data[x_variable, y_variable]

        plt.scatter(data[:, 0], data[:, 1], **kwargs)
        plt.xlabel(x_variable)
        plt.ylabel(y_variable)
        plt.title(f"{x_variable} vs {y_variable}")
        plt.show()
        return plt.gcf()

    
    def scatter_3d(self, x_variable: str, y_variable: str, z_variable: str, **kwargs) -> plt.Figure:
        '''
        Plots a 3D scatter plot of the dataset for the given
        x, y and z variables.

        Arguments:
        x_variable (str): The x variable to plot
        y_variable (str): The y variable to plot
        z_variable (str): The z variable to plot
        **kwargs: Arbitrary keyword arguments for plt.scatter

        Returns:
        None
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        data = self._data[x_variable, y_variable, z_variable]

        ax.scatter(data[:, 0], data[:, 1], data[:, 2])
        ax.set_xlabel(x_variable)
        ax.set_ylabel(y_variable)
        ax.set_zlabel(z_variable)
        plt.title(f"{x_variable} vs {y_variable} vs {z_variable}")
        plt.show()
        return fig