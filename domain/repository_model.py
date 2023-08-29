class Repository:
    ROW_HEADER = [
        "id",
        "name_with_owner",
        "url",
        "created_at",
        "updated_at",
        "primary_language",
        "stargazer_count",
        "pull_requests",
        "releases",
        "all_issues",
        "close_issues"
    ]

    def __init__(self, repo_json):
        self.id = repo_json["id"]
        self.name_with_owner = repo_json["nameWithOwner"]
        self.url = repo_json["url"]
        self.created_at = repo_json["details"]["createdAt"]
        self.updated_at = repo_json["details"]["updatedAt"]
        self.stargazer_count = repo_json["stargazerCount"]
        self.pull_requests = repo_json["details"]["pullRequests"]["totalCount"]
        self.releases = repo_json["details"]["releases"]["totalCount"]
        self.all_issues = repo_json["details"]["all_issues"]["totalCount"]
        self.close_issues = repo_json["details"]["close_issues"]["totalCount"]
        self.primary_language = "None"

        if repo_json["details"]["primaryLanguage"] is not None:
            self.primary_language = repo_json["details"]["primaryLanguage"]["name"]

    def get_string_row(self):
        return [
            self.id,
            self.name_with_owner,
            self.url,
            self.created_at,
            self.updated_at,
            self.primary_language,
            self.stargazer_count,
            self.pull_requests,
            self.releases,
            self.all_issues,
            self.close_issues,
        ]
