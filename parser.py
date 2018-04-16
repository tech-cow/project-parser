#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            repo_hash['type'] = "repo"
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
    语言为JavaScript的Repo信息
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

    var = ["var ", "LIST_DATA = "]
    var = map(str, var)
    line = "".join(var)
    print(line)

    with open('list_data.js', 'a+') as outfile:
         outfile.write(json.dumps(line, sort_keys = True, ensure_ascii=False))

    # Parse List
    g = Github('68ca7e33f2af4df750fea96e1626a04bc499cac1')
    repo_hash = {}
    res = []
    parse_python(g, repo_hash, [], res)
    parse_js(g, repo_hash, [], res)
    # with open('list_data.js', 'a') as outfile:
    #      outfile.write(json.dumps(res, indent=4,  sort_keys=True))

if __name__ == "__main__":
    main()
