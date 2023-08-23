import http

from settings import env_config
from string import Template
import requests

GITHUB_API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

QUERY_TOP_REPOS = """
{
  search(first: 101, type: REPOSITORY, query: "stars:>=10000") {
    edges {
      node {
        ... on Repository {
          owner {
            id
            login
          }
          id
          name
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
          all_issues: issues(first: 1) {
            totalCount
          }
          close_issues: issues(first: 1, states: CLOSED) {
            totalCount
          }
        }
      }
    }
  }
}
""")


def top_repos_query():
    request = requests.post(GITHUB_API_URL, json={'query': QUERY_TOP_REPOS}, headers=HEADERS)
    return request.json()


def repo_details_query(search_id):
    query = QUERY_REPO_DETAILS.substitute(search_id=search_id)
    request = requests.post(GITHUB_API_URL, json={'query': query}, headers=HEADERS)
    if request.status_code == http.HTTPStatus.OK:
        return request.json()
    else:
        raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")
