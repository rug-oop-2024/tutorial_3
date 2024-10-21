import pandas as pd
import numpy as np

from copy import deepcopy

from pathlib import Path


class Dataset:
    '''
    A class that handles datasets using pandas
    and provides an interface to access the data
    to the data_plotter module.
    '''
    def __init__(self, data_path: Path, *args, **kwargs) -> None:
        '''
        Constructs the dataset object by reading the data

        Arguments:
        data_path (Path): The path to the data file
        *args: Variable length argument list for pandas.read_csv
        **kwargs: Arbitrary keyword arguments for pandas.read_csv

        Returns:
        None
        '''
        self._data = pd.read_csv(data_path, *args, **kwargs)
        self._columns = self._data.columns

    def _filter_numerical_data(self) -> None:
        '''
        Filters out the non-numerical data from the dataset

        Returns:
        None
        '''
        self._data = self._data.select_dtypes(include=["number"])
    
    @property
    def data(self) -> pd.DataFrame:
        '''
        Getter for the _data attribute

        Returns:
        pd.DataFrame: The dataset
        '''
        return self._data.copy()

    @property
    def columns(self) -> list:
        '''
        Getter for the _columns attribute

        Returns:
        list: The columns of the dataset
        '''
        return deepcopy(self._columns)

    def __getitem__(self, *keys: str) -> np.ndarray:
        '''
        Returns specific column of the dataset

        Arguments:
        key (str): The column name

        Returns:
        pd.Series: The column of the dataset converted to numpy array
        '''
        if isinstance(keys[0], tuple):
            keys = list(keys[0])
        else:
            keys = list(keys)

        if not all(isinstance(key, str) for key in keys):
            raise TypeError(f"Key must be a string. Got {keys}" + 
                            f"of type {[type(key) for key in keys]}")
        return np.array(self._data[keys])

