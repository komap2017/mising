import pandas as pd


def main():
    csv = 'missing-people-in-russia\data-20140727-structure-20140727.csv'
    frame = pd.read_csv(csv)
    print(frame.head(10))


if __name__ == '__main__':
    main()
