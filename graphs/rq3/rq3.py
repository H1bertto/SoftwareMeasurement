import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../repository.csv')

    print("********** max ********** \n")
    print(df.iloc[df['releases'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['releases'].idxmin()])

    print("\n\n")

    print("median: " + str(df['releases'].median()))
    print("mean: " + str(df['releases'].mean()))
    print("std: " + str(df['releases'].std()))
    print("p90: " + str(df['releases'].quantile(q=0.9)))

    print("\n\n")

    correlation, p_value = pearsonr(df['releases'], df['stargazer_count'])
    print("correlation: " + str(correlation))
    print("p-value: " + str(p_value))

    df.plot(x='releases', y='stargazer_count', kind='scatter')
    plt.show()
