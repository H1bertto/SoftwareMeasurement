from Lab02.domain.generate_csv import generate_repository_csv, read_repository_csv
from git import Repo
import os


def lab2_start():
    # generate_repository_csv()
    last_line_cloned = None
    if os.path.exists('Lab02/last_line.txt'):
        with open('Lab02/last_line.txt', 'r', encoding='utf-8') as f:
            last_line_cloned = f.readline()
    repos = read_repository_csv(last_line_cloned)

    for repo in repos:
        Repo.clone_from(repo.url, "repos/" + repo.name_with_owner)
        f = open('Lab02/last_line.txt', 'w', encoding='utf-8')
        f.write(f'{repo.line}')
        f.flush()
        f.close()

    print('ok')
