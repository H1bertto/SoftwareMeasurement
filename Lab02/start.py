import subprocess

from Lab02.domain.generate_csv import generate_repository_csv, read_repository_csv
from Lab02.domain.ck_csv_service import CkCsvService
from Lab02.domain.ck_model import Ck
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


def temp():
    service = CkCsvService()
    service.start_writer()
    service.write_header()

    ck_analysis("airbnb/lottie-android", service)


def ck_analysis(repo, service):
    os.makedirs("./Lab02/ck-results/" + repo)
    subprocess.run(
        ["java", "-jar", "./Lab02/ck.jar", "./repos/" + repo, "true", "0", "False", "./Lab02/ck-results/" + repo + "/"])

    metrics = service.sum_ck_class(repo)
    service.write_row(Ck(metrics))
