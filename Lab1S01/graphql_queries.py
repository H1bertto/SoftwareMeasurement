from settings import env_config
import requests

GITHUB_API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

QUERY = """
{
    search(first: 100, type: REPOSITORY, query: "stars:>=10000") {
        repos: edges {
            repo: node {
                ... on Repository {
                    createdAt
                    name
                    url
                    id
                    stargazerCount
                }
            }
        }
    }
}
"""


def graphql_query():
    request = requests.post(GITHUB_API_URL, json={'query': QUERY}, headers=HEADERS)
    return request.json()
    # if request.status_code == statusCode:
    #     return request.json()
    # else:
    #     raise Exception(f"Unexpected status code returned: {request.status_code}")