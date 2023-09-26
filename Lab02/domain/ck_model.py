class Ck:
    ROW_HEADER = [
        "name",
        "cbo",
        "dit",
        "lcom",
    ]

    def __init__(self, metrics=None, ck_row=None):
        if metrics is not None:
            self.name = metrics["name"]
            self.cbo = metrics["cbo"]
            self.dit = metrics["dit"]
            self.lcom = metrics["lcom"]

        if ck_row is not None:
            self.name = ck_row[self.ROW_HEADER[0]]
            self.cbo = ck_row[self.ROW_HEADER[1]]
            self.dit = ck_row[self.ROW_HEADER[2]]
            self.lcom = ck_row[self.ROW_HEADER[3]]

    def get_string_row(self):
        return [
            self.name,
            self.cbo,
            self.dit,
            self.lcom,
        ]
