import requests
import time

from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

for i in range(1, 30):
    url = 'https://github.com/search?o=desc&p=' + str(i) + '&q=hexo-theme&s=stars&type=Repositories'
    r = requests.get(url, headers=headers)
    
    text = r.text
    soup = BeautifulSoup(text, "html.parser")

    divs = soup.find_all('li', attrs={'class': 'repo-list-item'})
    for d in divs:
        print(d)
        star = d.find('a', attrs={'class': 'muted-link'}).text.strip()
        # print(star)

        desc = d.find('p', attrs={'class': 'mb-1'}).text.strip()
        # print(desc)

        name = d.find('a', attrs={'class': 'v-align-middle'}).text.strip()
        # print(name)

        href = 'https://www.github.com' +  d.find('a', attrs={'class': 'v-align-middle'})['href']
    print('finish page {}'.format(i))