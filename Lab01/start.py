from Lab01.domain.generate_csv import read_repository_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def lab1_start():
    # generate_repository_csv()
    repositories = read_repository_csv()

    languages = {}
    for repo in repositories:
        if repo.primary_language in languages:
            languages[repo.primary_language] += 1
        else:
            languages[repo.primary_language] = 1

    keys = list(languages.keys())
    values = list(languages.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    lan = []
    c = []
    for key in languages:
        if languages[key] > 4:
            lan.append(key)
            c.append(languages[key])

    frame = {
        'languages': lan,
        'count': c
    }

    df = pd.DataFrame.from_dict(frame)
    df.plot.bar(x='languages', y='count')

    plt.tight_layout()
    plt.show()
    print('Finished')