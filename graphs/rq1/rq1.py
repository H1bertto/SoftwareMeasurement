import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../repository.csv')

    print("********** max ********** \n")
    print(df.iloc[df['created_at'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['created_at'].idxmin()])

    print("\n\n")

    print("median: " + str(df['created_at'].median()))
    print("mean: " + str(df['created_at'].mean()))
    print("std: " + str(df['created_at'].std()))
    print("p90: " + str(df['created_at'].quantile(q=0.9)))

    print("\n\n")

    correlation, p_value = pearsonr(df['created_at'], df['stargazer_count'])
    print("correlation: " + str(correlation))
    print("p-value: " + str(p_value))

    df.plot(x='created_at', y='stargazer_count', kind='scatter')
    plt.show()
