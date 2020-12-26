from urllib.request import urlopen
from html.parser import HTMLParser

class Scraper(HTMLParser):
    in_h3 = False
    in_link = False
    
    def handle_starttag(self,tag,attrs):
        #print("Encountered a start tag:", tag)
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True
        if tag == 'a' and 'href' in attrs:
            self.in_link=True
            self.chunks = []
            self.url = attrs['href']
    
    def handle_data(self,data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self,tag):
        #print("Encountered an end tag :", tag)
        if tag == 'h3':
             self.in_h3 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print(''.join(self.chunks),self.url)
            self.in_link = False

text = str(urlopen('https://www.seek.com.au/jobs').read())
parser = Scraper()
parser.feed(text)
parser.close()
