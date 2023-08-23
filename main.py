from Lab1S01.graphql_queries import repo_details_query, top_repos_query


def get_top_repos():
    data = top_repos_query()['data']['search']['edges']
    repos = []
    for repo_node in data:
        repo = repo_node['node']
        search_id = repo['owner']['login'] + "/" + repo['name']
        details = repo_details_query(search_id)['data']['search']['edges'][0]['node']
        repo['details'] = details
        repos.append(repo)
    return repos





if __name__ == '__main__':
    top_repos = get_top_repos()
    print('ok')
