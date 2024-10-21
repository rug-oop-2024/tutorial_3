import argparse

from pathlib import Path

from data_plotter.data_handler import Dataset
from data_plotter.data_plotter import DataPlotter

def parse_args():
    parser = argparse.ArgumentParser(description="A simple data plotter")
    parser.add_argument("data_path", type=str, help="The path to the data file")
    return parser.parse_args()

def main():
    args = parse_args()

    data_path = Path(args.data_path)

    data = Dataset(data_path)
    plotter = DataPlotter(data)
    
    plotter.hist_1d("petal.width")
    plotter.scatter_2d("petal.width", "petal.length")
    plotter.scatter_3d("petal.width", "petal.length", "sepal.width")


if __name__ == "__main__":
    main()