from github import Github
import pprint
import json

def parse_python(g, repo_hash, temp_list, res):
    '''
    语言为Python的Repo信息
    根据星星进行从大到小排序
    '''
    res.append({
                "type": "category",
                "name": "Python",
               })

    for repo in g.get_user().get_repos():
        if repo.stargazers_count > 0 and repo.language == 'Python':
            repo_hash['types'] = "repo"
            repo_hash['name'] = repo.name
            repo_hash['description'] = repo.description
            repo_hash['stars'] = repo.stargazers_count
            repo_hash['forks'] = repo.forks_count
            repo_hash['lang'] = repo.language
            repo_hash['url'] = repo.html_url
            temp_list.append(repo_hash)
            repo_hash = {}

    temp_list = sorted(temp_list, key=lambda d: d["stars"])
    temp_list = temp_list[::-1]
    for repo in temp_list:
        res.append(repo)

def parse_js(g, repo_hash, temp_list, res):
    '''
    语言为Python的Repo信息
    根据星星进行从大到小排序
    '''
    res.append({
                "type": "category",
                "name": "JavaScript",
               })

    for repo in g.get_user().get_repos():
        if repo.stargazers_count > 0 and repo.language == 'JavaScript':
            repo_hash['types'] = "repo"
            repo_hash['name'] = repo.name
            repo_hash['description'] = repo.description
            repo_hash['stars'] = repo.stargazers_count
            repo_hash['forks'] = repo.forks_count
            repo_hash['lang'] = repo.language
            repo_hash['url'] = repo.html_url
            temp_list.append(repo_hash)
            repo_hash = {}

    temp_list = sorted(temp_list, key=lambda d: d["stars"])
    temp_list = temp_list[::-1]
    for repo in temp_list:
        res.append(repo)


def main():
    g = Github('3ba11a4df313ad1b810814d1d648d3ab250195e4')
    repo_hash = {}
    res = []
    parse_python(g, repo_hash, [], res)
    parse_js(g, repo_hash, [], res)

    with open('log.js', 'w') as outfile:
        json.dump(res, outfile)

if __name__ == "__main__":
    main()
