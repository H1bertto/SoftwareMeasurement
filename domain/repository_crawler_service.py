from external.github_api import GithubApi


class RepositoryCrawlerService:

    def __init__(self):
        self.github_api = GithubApi()

    def crawl(self):
        data_json = self.github_api.top_repos_query()
        data = data_json['data']['search']['edges']
        repos = []

        count = 0
        for node in data:
            repo = node['node']
            search_id = repo['nameWithOwner']
            print("{}. Getting details for {}".format(count, search_id))
            details = self.github_api.repo_details_query(search_id)['data']['search']['edges'][0]['node']
            repo['details'] = details
            repos.append(repo)
            count += 1

        return repos
