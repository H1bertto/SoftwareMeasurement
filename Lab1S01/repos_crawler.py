from Lab1S01.graphql_queries import repo_details_query, top_repos_query


def get_top_repos():
    data_json = top_repos_query()
    data = data_json['data']['search']['edges']
    repos = []

    blacklist = 0

    for node in data:
        repo = node['node']
        search_id = repo['nameWithOwner']
        print("{}. Getting details for {}".format(node, search_id))
        details = repo_details_query(search_id)['data']['search']['edges'][0]['node']
        repo['details'] = details
        repos.append(repo)

    data.pop(blacklist)
    return repos