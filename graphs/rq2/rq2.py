import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../repository.csv')

    print("********** max ********** \n")
    print(df.iloc[df['pull_requests'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['pull_requests'].idxmin()])

    print("\n\n")

    print("median: " + str(df['pull_requests'].median()))
    print("mean: " + str(df['pull_requests'].mean()))
    print("std: " + str(df['pull_requests'].std()))
    print("p90: " + str(df['pull_requests'].quantile(q=0.9)))

    print("\n\n")

    correlation, p_value = pearsonr(df['pull_requests'], df['stargazer_count'])
    print("correlation: " + str(correlation))
    print("p-value: " + str(p_value))

    df.plot(x='pull_requests', y='stargazer_count', kind='scatter')
    plt.show()
