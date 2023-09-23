from Lab02.domain.repository_model import Repository
from settings import BASE_DIR
import pandas as pd
import csv
import os


class RepositoryCsvService:
    FILE_NAME = "repository.csv"
    READING_MODE = "READING"
    WRITING_MODE = "WRITING"

    def __init__(self):
        self.mode = None
        self.writer = None
        self.reader = None
        self.file = None

    def reset_internal(self):
        self.file.close()
        self.mode = None
        self.writer = None
        self.reader = None
        self.file = None

    def remove_file(self):
        if self.mode is not None:
            self.reset_internal()
        if os.path.exists(self.FILE_NAME):
            os.remove(self.FILE_NAME)

    def start_writer(self):
        if self.mode is not None:
            self.reset_internal()

        self.mode = self.WRITING_MODE
        self.file = open(self.FILE_NAME, "w", newline='', encoding='utf-8')
        self.writer = csv.writer(self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def write_header(self):
        self.writer.writerow(Repository.ROW_HEADER)

    def write_row(self, repository: Repository):
        self.writer.writerow(repository.get_string_row())
        self.file.flush()

    def start_reader(self, skip_rows=None):
        if self.mode is not None:
            self.reset_internal()

        self.mode = self.READING_MODE
        file_path = f'{BASE_DIR}/Lab02/{self.FILE_NAME}'
        self.file = pd.read_csv(file_path, encoding='utf-8', skiprows=skip_rows,)
        # self.file = open(file_path, "r", newline='', encoding='utf-8')
        # self.reader = csv.DictReader(self.file)
        self.reader = self.file.to_dict(orient='records')

    def read_all(self):
        repositories = []
        for row in self.reader:
            repositories.append(Repository(repo_row=row, line=self.reader.index(row)+1))
        return repositories
