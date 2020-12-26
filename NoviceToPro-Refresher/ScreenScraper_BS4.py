from urllib.request import urlopen
from bs4 import BeautifulSoup

text =  str(urlopen('https://en.wikipedia.org/wiki/Python_%28programming_language%29').read())
soup = BeautifulSoup(text, features="html.parser")

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = link[0]
    jobs.add(link.string, link['href'])

print('\n'.join(sorted(jobs, key=lambda s:s.lower())))
