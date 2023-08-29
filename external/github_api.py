import http

from settings import env_config
from string import Template
import requests


class GithubApi:
    URL = "https://api.github.com/graphql"
    HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

    QUERY_TOP_REPOS = """
    {
      search(first: 100, type: REPOSITORY, query: "stars:>=10000") {
        edges {
          node {
            ... on Repository {
              id
              nameWithOwner
              url
              stargazerCount
            }
          }
        }
      }
    }
    """

    QUERY_REPO_DETAILS = Template("""
    {
      search(first: 1, type: REPOSITORY, query: "repo:$search_id") {
        edges {
          node {
            ... on Repository {
              createdAt
              pullRequests(first: 1, states: MERGED) {
                totalCount
              }
              releases(first: 1) {
                totalCount
              }
              updatedAt
              primaryLanguage {
                name
              }
              all_issues: issues {
                totalCount
              }
              close_issues: issues(states: [CLOSED]) {
                totalCount
              }
            }
          }
        }
      }
    }
    """)

    def top_repos_query(self):
        request = requests.post(self.URL, json={'query': self.QUERY_TOP_REPOS}, headers=self.HEADERS)
        if request.status_code == http.HTTPStatus.OK:
            return request.json()
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")

    def repo_details_query(self, search_id):
        query = self.QUERY_REPO_DETAILS.substitute(search_id=search_id)
        request = requests.post(self.URL, json={'query': query}, headers=self.HEADERS, timeout=None)
        if request.status_code == http.HTTPStatus.OK:
            return request.json()
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")
