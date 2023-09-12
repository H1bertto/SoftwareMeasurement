import http
import json

from Lab02.settings import env_config
from string import Template
import requests


class GithubApi:
    URL = "https://api.github.com/graphql"
    HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

    QUERY_TOP_REPOS = Template("""
    {
      search(first: 100, type: REPOSITORY, query: "language:java stars:>2500 sort:stars" $pagination) {
        pageInfo {
          hasNextPage
          endCursor
        }
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
    """)

    QUERY_REPO_DETAILS = Template("""
    {
      search(first: 1, type: REPOSITORY, query: "repo:$search_id") {
        edges {
          node {
            ... on Repository {
              createdAt
              releases {
                totalCount
              }
            }
          }
        }
      }
    }
    """)

    def top_repos_query(self, cursor=""):
        pagination = cursor
        if cursor != "":
            pagination = Template(""", after: "$cursor" """).substitute(cursor=cursor)

        query = self.QUERY_TOP_REPOS.substitute(pagination=pagination)
        request = requests.post(self.URL, json={'query': query}, headers=self.HEADERS, timeout=60)
        if request.status_code == http.HTTPStatus.OK:
            try:
                response_json = request.json()
            except json.JSONDecodeError:
                response_json = {
                    'error': 'JSON Error',
                    'info': request.text
                }
            return response_json
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")

    def repo_details_query(self, search_id):
        query = self.QUERY_REPO_DETAILS.substitute(search_id=search_id)
        request = requests.post(self.URL, json={'query': query}, headers=self.HEADERS, timeout=60)
        if request.status_code == http.HTTPStatus.OK:
            try:
                response_json = request.json()
            except json.JSONDecodeError:
                response_json = {
                    'error': 'JSON Error',
                    'info': request.text
                }

            #temp
            if len(response_json['data']['search']['edges']) == 0:
                print('wtf')
            #temp

            return response_json
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")
