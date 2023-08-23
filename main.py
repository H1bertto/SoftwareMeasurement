from Lab1S01.graphql_queries import repo_details_query, top_repos_query


def get_top_repos():
    data = top_repos_query()['data']['search']['edges']
    repos = []

    blacklist = 0

    for i in range(len(data)):
        repo = data[i]['node']
        search_id = repo['owner']['login'] + "/" + repo['name']

        # blacklist
        if search_id == "microsoft/vscode":
            blacklist = i
            continue

        print("{}. Getting details for {}".format(i, search_id))
        details = repo_details_query(search_id)['data']['search']['edges'][0]['node']
        repo['details'] = details
        repos.append(repo)

    data.pop(blacklist)
    return repos


if __name__ == '__main__':
    top_repos = get_top_repos()

    # test = repo_details_query('microsoft/vscode')
    print('ok')
