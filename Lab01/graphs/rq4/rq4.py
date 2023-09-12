import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../../repository.csv')

    print("********** max ********** \n")
    print(df.iloc[df['updated_at'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['updated_at'].idxmin()])

    print("\n\n")

    print("median: " + str(df['updated_at'].median()))
    print("mean: " + str(df['updated_at'].mean()))
    print("std: " + str(df['updated_at'].std()))
    print("p90: " + str(df['updated_at'].quantile(q=0.9)))

    print("\n\n")

    correlation, p_value = pearsonr(df['updated_at'], df['stargazer_count'])
    print("correlation: " + str(correlation))
    print("p-value: " + str(p_value))

    df.plot(x='updated_at', y='stargazer_count', kind='scatter')
    plt.show()
