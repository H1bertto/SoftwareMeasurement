import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../repository.csv')

    print("********** max ********** \n")
    print(df.iloc[df['issues_rate'].idxmax()])

    print("\n\n********** min ********** \n")
    print(df.iloc[df['issues_rate'].idxmin()])

    print("\n\n")

    print("median: " + str(df['issues_rate'].median()))
    print("mean: " + str(df['issues_rate'].mean()))
    print("std: " + str(df['issues_rate'].std()))
    print("p90: " + str(df['issues_rate'].quantile(q=0.9)))

    print("\n\n")

    correlation, p_value = pearsonr(df['issues_rate'], df['stargazer_count'])
    print("correlation: " + str(correlation))
    print("p-value: " + str(p_value))

    df.plot(x='issues_rate', y='stargazer_count', kind='scatter')
    plt.show()
