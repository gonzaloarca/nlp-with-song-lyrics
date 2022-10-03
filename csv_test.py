import pandas as pd


if __name__ == "__main__":
    print(pd.read_csv("charts.csv", sep=",")[["lyrics"]])
