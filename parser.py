from github import Github
import pprint

g = Github('2f758268172e40756c4d524d15f0ffd9451f170c')

repo_hash = {}

res = []

for repo in g.get_user().get_repos():
    repo_hash['name'] = repo.name
    repo_hash['description'] = repo.description
    repo_hash['stars'] = repo.stargazers_count
    repo_hash['forks'] = repo.forks_count
    repo_hash['lang'] = repo.language
    repo_hash['url'] = repo.html_url
    res.append(repo_hash)
    repo_hash = {}


pprint.pprint(res)
