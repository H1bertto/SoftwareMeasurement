from dateutil.relativedelta import relativedelta
from datetime import datetime


class Repository:
    ROW_HEADER = [
        "id",
        "name_with_owner",
        "url",
        "created_at",
        "stargazer_count",
        "releases",
    ]

    def __init__(self, repo_json=None, repo_row=None):
        if repo_json is not None:
            self.id = repo_json["id"]
            self.name_with_owner = repo_json["nameWithOwner"]
            self.url = repo_json["url"]
            self.stargazer_count = repo_json["stargazerCount"]
            self.releases = repo_json["details"]["releases"]["totalCount"]

            now = datetime.utcnow()

            created_at = datetime.strptime(repo_json["details"]["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
            self.created_at = relativedelta(now, created_at).years

        if repo_row is not None:
            self.id = repo_row[self.ROW_HEADER[0]]
            self.name_with_owner = repo_row[self.ROW_HEADER[1]]
            self.url = repo_row[self.ROW_HEADER[2]]
            self.created_at = repo_row[self.ROW_HEADER[3]]
            self.stargazer_count = repo_row[self.ROW_HEADER[4]]
            self.releases = repo_row[self.ROW_HEADER[5]]

    def get_string_row(self):
        return [
            self.id,
            self.name_with_owner,
            self.url,
            self.created_at,
            self.stargazer_count,
            self.releases,
        ]
