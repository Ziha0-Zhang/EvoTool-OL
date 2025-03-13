import requests
from bs4 import BeautifulSoup
import json
import os
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

repoURL = "TUDB-Labs/MixLoRA"

# the URL of the target repo to scrape
url = f"https://github.com/{repoURL}"

# download the target page
page = requests.get(url, headers=headers)


# parse the HTML document returned by the server
soup = BeautifulSoup(page.text, 'html.parser')

# initialize the object that will contain
repo = {}

# repo scraping logic
name_html_element = soup.select_one('[itemprop="name"]')
name = name_html_element.get_text().strip() if name_html_element else "未知"

git_branch_icon_html_element = soup.select_one('.octicon-git-branch')
main_branch = "main"  # 默认值
if git_branch_icon_html_element:
    main_branch_html_element = git_branch_icon_html_element.find_next_sibling('span')
    if main_branch_html_element:
        main_branch = main_branch_html_element.get_text().strip()

# 修改这部分代码，添加错误检查
boxheader_html_element = soup.select_one('.Box .Box-header')
latest_commit = ""
commits = "0"

if boxheader_html_element:
    relative_time_html_element = boxheader_html_element.select_one('relative-time')
    if relative_time_html_element and 'datetime' in relative_time_html_element.attrs:
        latest_commit = relative_time_html_element['datetime']
    
    history_icon_html_element = boxheader_html_element.select_one('.octicon-history')
    if history_icon_html_element:
        commits_span_html_element = history_icon_html_element.find_next_sibling('span')
        if commits_span_html_element:
            commits_html_element = commits_span_html_element.select_one('strong')
            if commits_html_element:
                commits = commits_html_element.get_text().strip().replace(',', '')

# 尝试使用不同的选择器查找仓库信息
bordergrid_html_element = soup.select_one('.BorderGrid')
description = ""
stars = "0"
watchers = "0"
forks = "0"

if bordergrid_html_element:
    about_html_element = bordergrid_html_element.select_one('h2')
    if about_html_element:
        description_html_element = about_html_element.find_next_sibling('p')
        if description_html_element:
            description = description_html_element.get_text().strip()
    
    star_icon_html_element = bordergrid_html_element.select_one('.octicon-star')
    if star_icon_html_element:
        stars_html_element = star_icon_html_element.find_next_sibling('strong')
        if stars_html_element:
            stars = stars_html_element.get_text().strip().replace(',', '')
    
    eye_icon_html_element = bordergrid_html_element.select_one('.octicon-eye')
    if eye_icon_html_element:
        watchers_html_element = eye_icon_html_element.find_next_sibling('strong')
        if watchers_html_element:
            watchers = watchers_html_element.get_text().strip().replace(',', '')
    
    fork_icon_html_element = bordergrid_html_element.select_one('.octicon-repo-forked')
    if fork_icon_html_element:
        forks_html_element = fork_icon_html_element.find_next_sibling('strong')
        if forks_html_element:
            forks = forks_html_element.get_text().strip().replace(',', '')

# build the URL for README.md and download it
readme_url = f'https://raw.githubusercontent.com/{repoURL}/refs/heads/main/README.md'
readme_page = requests.get(readme_url, headers=headers)
print(readme_url)
print(readme_page)
readme = None
# if there is a README.md file
if readme_page.status_code != 404:
    readme = readme_page.text

# store the scraped data 
repo['name'] = name
repo['latest_commit'] = latest_commit
repo['commits'] = commits
repo['main_branch'] = main_branch
repo['description'] = description
repo['stars'] = stars
repo['watchers'] = watchers
repo['forks'] = forks
repo['readme'] = readme

# export the scraped data to a repo.json output file
with open('repo.json', 'w') as file:
    json.dump(repo, file, indent=4)