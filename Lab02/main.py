from Lab02.domain.generate_csv import generate_repository_csv, read_repository_csv
from git import Repo


if __name__ == '__main__':
    # generate_repository_csv()
    repos = read_repository_csv()

    for repo in repos:
        Repo.clone_from(repo.url, "repos/" + repo.name_with_owner)

    print('ok')
