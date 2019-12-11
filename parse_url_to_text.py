from bs4 import BeautifulSoup
import requests
import re
import spacy
import html2text
nlp = spacy.load("en_core_web_sm")


def get_html_file(url):
    if not url.startswith("http"):
        url = "https://" + url
    res = requests.get(url)
    html_page = res.text
    # print(html_page)
    # print(html_page)
    return html_page


def html_to_text(html):
    # soup = BeautifulSoup(html, features="html.parser")
    # # text = soup.find_all(text=True)
    # blacklist = [
    #     # "script",
    #     # "style",
    #     # "aside",
    #     # "head",


    #     '[document]',
    #     'noscript',
    #     'header',
    #     # 'html',
    #     'meta',
    #     'head', 
    #     'input',
    #     'script',
    # ]
    # for script in soup(blacklist):
    #     script.extract()
    # # print(soup)
    # text = soup.get_text()

    # text = ' '.join(text.split())
    # text = text.replace("\t", " ")
    # text = " ".join(re.split(r'[\n\t]+', text))
    # article = nlp(text)

    # ##labels = [x.label_ for x in article.ents]
    # ##Counter(labels)

    # ##items = [x.text for x in article.ents]
    # ##Counter(items).most_common(3)

    # sentences = [x.text for x in article.sents]
    # output = "".join(str(sentences))
    # return output
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    return h.handle(html)
    
def parse_body_text_from_text_version(text):
    text = text.split("\n")
    print(text)




link = "https://www.bbc.com/news/world-asia-50723352"
# link = "https://www.nytimes.com/2019/12/09/us/politics/fbi-ig-report-russia-investigation.html"
html = get_html_file(link)
text = html_to_text(html)
parse_body_text_from_text_version(text)
# print(text)
