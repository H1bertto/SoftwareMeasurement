import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../result.csv')

    print("********** max ********** \n")
    print(df.iloc[df['stargazer_count'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['stargazer_count'].idxmin()])

    print("\n\n")

    print("median: " + str(df['stargazer_count'].median()))
    print("mean: " + str(df['stargazer_count'].mean()))
    print("std: " + str(df['stargazer_count'].std()))
    print("p90: " + str(df['stargazer_count'].quantile(q=0.9)))

    print("\n\n")

    df = df[df.stargazer_count < df.stargazer_count.quantile(.80)]
    df = df[df.qi < df.qi.quantile(.80)]

    # correlation, p_value = pearsonr(df['stargazer_count'], df['stargazer_count'])
    # print("correlation: " + str(correlation))
    # print("p-value: " + str(p_value))

    df.plot(x='stargazer_count', y='qi', kind='scatter')
    plt.show()
