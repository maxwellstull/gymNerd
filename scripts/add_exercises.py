import pandas as pd

def main():
    # Read
    df = pd.read_csv("data/db.csv", header=0, quotechar="\"")

    print(list(df))
    # Add exercise
    inputs = {}
    for i in list(df):
        inputs[i] = [input(i + ": " )]
    print(inputs)
    df_new = pd.DataFrame.from_dict(inputs)
    df = pd.concat([df, df_new])
    # Write
    df.to_csv("data/db.csv", index=False)


if __name__ == "__main__":
    main()