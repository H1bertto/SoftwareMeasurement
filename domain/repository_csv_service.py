from domain.repository_model import Repository
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
