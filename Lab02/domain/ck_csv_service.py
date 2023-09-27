from Lab02.domain.ck_model import Ck
from settings import BASE_DIR
import pandas as pd
import csv
import os


class CkCsvService:
    PATH = f'{BASE_DIR}/Lab02/ck-results/'
    FILE_NAME = f'{BASE_DIR}/Lab02/ck-results/ck.csv'
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
        self.file = open(self.FILE_NAME, "a", newline='', encoding='utf-8')
        self.writer = csv.writer(self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def write_header(self):
        self.writer.writerow(Ck.ROW_HEADER)

    def write_row(self, ck: Ck):
        self.writer.writerow(ck.get_string_row())
        self.file.flush()

    def start_reader(self):
        if self.mode is not None:
            self.reset_internal()

        self.mode = self.READING_MODE
        self.file = pd.read_csv(self.FILE_NAME, encoding='utf-8')
        self.reader = self.file.to_dict(orient='records')

    def read_all(self):
        metrics = []
        for row in self.reader:
            metrics.append(Ck(ck_row=row))
        return metrics

    def sum_ck_class(self, name):
        file = pd.read_csv(self.PATH + name + "/class.csv", encoding='utf-8')

        cbo_sum = 0
        dit_sum = 0
        lcom_sum = 0
        count = 0

        for row in file.to_dict(orient='records'):
            cbo_sum += row["cbo"]
            dit_sum += row["dit"]
            lcom_sum += row["lcom"]
            count += 1

        if count > 0:
            return {"name": name, "cbo": cbo_sum / count, "dit": dit_sum / count, "lcom": lcom_sum / count}
        else:
            return {"name": name, "cbo": 0, "dit": 0, "lcom": 0}


    def read_ck_method(self, repo):
        file = pd.read_csv(self.PATH + repo + "/method.csv", encoding='utf-8')

        metrics = []

        for row in file.to_dict(orient='records'):
            metrics.append({"cbo": row["cbo"]})
        return metrics
