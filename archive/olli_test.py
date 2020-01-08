# ### https://www.bbc.com/news/world-asia-50741094

# ### URLISTA artikkelin n:nnen lauseen dep ja ent esitys


# from bs4 import BeautifulSoup
# import requests
# import re
# import spacy

# import nltk
# from stat_parser import Parser

# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
# nlp = spacy.load("en_core_web_sm")


# def url_to_string(url):
#     res = requests.get(url)
#     html = res.text
#     soup = BeautifulSoup(html, 'html.parser')
#     for script in soup(["script", "style", 'aside']):
#         script.extract()
#     return " ".join(re.split(r'[\n\t]+', soup.get_text()))
    
    
# ny_bb = url_to_string("https://www.bbc.com/news/world-asia-50741094")
# article = nlp(ny_bb)
# len(article.ents)

# ##labels = [x.label_ for x in article.ents]
# ##Counter(labels)

# ##items = [x.text for x in article.ents]
# ##Counter(items).most_common(3)

# sentences = [x.text for x in article.sents]
# print("".join(str(sentences)))




# ##displacy.serve(nlp(str(sentences[20])), style='dep', options = {'distance': 120})
# displacy.serve(nlp(str(sentences)), style='ent', options = {'distance': 120})

from html.parser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import requests

def get_html_file(url):
    if not url.startswith("http"):
        url = "https://" + url
    res = requests.get(url)
    html_page = res.text
    # print(html_page)
    # print(html_page)
    return html_page

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


def main():
    text = get_html_file("https://www.bbc.com/news/world-asia-50741094")
    # text = r'''
    #     <html>
    #         <body>
    #             <b>Project:</b> DeHTML<br>
    #             <b>Description</b>:<br>
    #             This small script is intended to allow conversion from HTML markup to 
    #             plain text.
    #         </body>
    #     </html>
    # '''
    print(dehtml(text))


if __name__ == '__main__':
    main()