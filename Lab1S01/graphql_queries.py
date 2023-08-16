from settings import env_config
import requests

GITHUB_API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

QUERY_TOP_REPOS = """
{
  search(first: 100, type: REPOSITORY, query: "stars:>=10000") {
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

QUERY_REPO = """
{
  search(first: 1, type: REPOSITORY, query: "repo:vuejs/vue") {
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
"""


def graphql_query():
    request = requests.post(GITHUB_API_URL, json={'query': QUERY_TOP_REPOS}, headers=HEADERS)
    return request.json()
    # if request.status_code == statusCode:
    #     return request.json()
    # else:
    #     raise Exception(f"Unexpected status code returned: {request.status_code}")
