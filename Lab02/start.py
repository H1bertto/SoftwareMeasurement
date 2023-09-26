import subprocess

from Lab02.domain.generate_csv import generate_repository_csv, read_repository_csv
from Lab02.domain.ck_csv_service import CkCsvService
from Lab02.domain.ck_model import Ck
from settings import BASE_DIR
from git import Repo
import shutil
import os


REPOS_PATH = f"{BASE_DIR}/Lab02/repos/"


def lab2_start():
    # generate_repository_csv()
    last_line_cloned = None
    if os.path.exists('Lab02/last_line.txt'):
        with open('Lab02/last_line.txt', 'r', encoding='utf-8') as f:
            last_line_cloned = f.readline()
    repos = read_repository_csv(last_line_cloned)

    step_to_pause_clone = 10
    for repo in repos:
        Repo.clone_from(repo.url, "repos/" + repo.name_with_owner)
        f = open('Lab02/last_line.txt', 'w', encoding='utf-8')
        f.write(f'{repo.line}')
        f.flush()
        f.close()
        if (repo.line % step_to_pause_clone) == 0:
            run_ck_analysis()
            remove_cloned_repos()


def start_ck():
    service = CkCsvService()
    service.start_writer()
    service.write_header()
    return service


def ck_analysis(repo, service):
    os.makedirs("./Lab02/ck-results/" + repo)
    subprocess.run(
        ["java", "-jar", "./Lab02/ck.jar", "./repos/" + repo, "true", "0", "False", "./Lab02/ck-results/" + repo + "/"])

    metrics = service.sum_ck_class(repo)
    service.write_row(Ck(metrics))


def run_ck_analysis():
    service = start_ck()
    repos_path = f"{BASE_DIR}/Lab02/repos/"
    if os.path.exists(repos_path):
        for dir_name in os.listdir(repos_path):
            ck_analysis(dir_name, service)
    else:
        raise Exception(f"Path not found: repos/")


def remove_cloned_repos():
    repos_path = f"{BASE_DIR}/Lab02/repos/"
    if os.path.exists(repos_path):
        for dir_name in os.listdir(repos_path):
            dir_path = os.path.join(repos_path, dir_name)
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
    else:
        raise Exception(f"Path not found: repos/")
