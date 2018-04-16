from github import Github
import pprint

g = Github('a71b6195f95b23cb5909f2f5b747a0fce5ab37ee')
repo_hash = {}
repo_list = []
res = []

def parse_python():
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
            res.append(repo_list)
            repo_hash = {}

    repo_list = sorted(repo_list, key=lambda d: d["stars"])
    for repo in repo_list[::-1]:
        res.append(repo)





print(len(res))
