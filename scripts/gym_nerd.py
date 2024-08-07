import pandas as pd
from nicegui import ui

def main():
    df = pd.read_csv("data/db.csv", header=0, quotechar="\"")




if __name__ == "__main__":
    main()