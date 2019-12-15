## In case If you have an error mentioning spacy.strings.StringStore size changed, may indicate binary incompatibility
## pip3 uninstall neuralcoref
## pip3 uninstall spacy
## pip3 install spacy==2.1.6
## pip3 install --upgrade setuptools
## pip3 install cython==0.29.14
## pip3 install https://github.com/huggingface/neuralcoref/archive/master.zip
## python -m spacy download en

## Ehkä merkitystä numpy==1.17.2

##check this out
##https://huggingface.co/coref/?text=Students%20are%20hungry%20but%20they%20feel%20the%20need%20for%20speed.


import spacy
import neuralcoref

from bs4 import BeautifulSoup
import requests
import re
import spacy
import html2text

def parse_body_text_from_url(link):
    """
    Fetches the HTML version of a BBC page and parses it to text.
    """

    html = _get_html_file(link)
    text = _html_to_text(html)
    text = _parse_body_text_from_text_version(text)
    return text

def _get_html_file(url):
    """
    Gets a HTML version of the web page given in the 'url' argument.
    Returns HTML version as a string.
    """
    if not url.startswith("http"):
        url = "https://" + url
    res = requests.get(url)
    html_page = res.text
    # print(html_page)
    # print(html_page)
    return html_page


def _html_to_text(html):
    """
    Parses HTML page to text. Returns a string.
    """
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_videos = True
    return h.handle(html)


def _parse_body_text_from_text_version(text):
    """
    Takes the full text and removes clutter. Returns parsed text
    """

    text_as_list = text.split("\n")
    for idx, row in enumerate(text_as_list):
        if "## related topics" in row.lower():
            text_as_list = text_as_list[:idx]
            break
        if "article share tools" in row.lower():
            text_as_list = text_as_list[:idx]
            break
        # blacklist = [
        #     "    * ",
        #     "    * ",

        # ]
    for idx, row in enumerate(text_as_list):
        if row.startswith(
            (
            "    * ",
            "Share this with",
            "  * Share this with"
        )
        ):
            text_as_list.pop(idx)
    for idx, row in enumerate(text_as_list):
        if row == text_as_list[idx-2] and row != " " and row != "":
            # print(row)
            text_as_list = text_as_list[idx:]
            break

    for idx, row in enumerate(text_as_list):
        if "Close share panel" in row:
            text_as_list = text_as_list[idx+3:]
            break

    # print(text_as_list)
    # print("\n".join(text_as_list))
    text = "\n".join(text_as_list)
    
    # convert symbol text to avoid problems in ne indexing. possible
    # double space is fixed by later replaces
    text = text.replace("%", " percent ")
    
    # remove multiple newlines to normal dot
    while "\n\n" in text:
        text = text.replace("\n\n", ". ")

    # remove multiple dots resulting from previous operation
    while ".." in text:
        text = text.replace("..", ".")

    # remove multiple space
    while "  " in text:
        text = text.replace("  ", " ")
    
    # replace newlines with spaces
    while "\n" in text:
        text = text.replace("\n", " ")

    # replace prefix with more machine-readable form
    text = text.replace("pro-", "pro ")
    text = text.replace("anti-", "anti ")
    
    text = text.replace("one-", "one ")
    text = text.replace("two-", "two ")
    text = text.replace("three-", "three ")
    text = text.replace("four-", "four ")
    text = text.replace("five-", "five ")
    text = text.replace("six-", "six ")
    text = text.replace("seven-", "seven ")
    text = text.replace("eight-", "eight ")
    text = text.replace("nine-", "nine ")
    text = text.replace("ten-", "ten ")

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number+"km" in text:
            text = text.replace(number+"km", number+" km")



    return text
    # print(text_as_list)

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
link = "https://www.bbc.com/news/world-europe-50740324"
##doc1 = "Students are hungry but they feel the need for speed."
##doc1 = "Students are hungry but they feel the need for speed. Students really like John. John is a sick bastard and he is white."
##doc1 = "The 16-year-old is the youngest person to be chosen by the magazine in a tradition that started in 1927. Speaking at a UN climate change summit in Madrid before the announcement, she urged world leaders to stop using creative PR to avoid real action. The next decade would define the planet's future, she said. Last year, the teenager started an environmental strike by missing lessons most Fridays to protest outside the Swedish parliament building. It sparked a worldwide movement that became popular with the hashtag #FridaysForFuture. Since then, she has become a strong voice for action on climate change, inspiring millions of students to join protests around the world. Earlier this year, she was nominated as a candidate for the Nobel Peace Prize."
doc1 = parse_body_text_from_url(link)
doc1 = nlp(doc1)
print(doc1._.coref_clusters)  ##All the clusters of corefering mentions in the doc


##for ent in doc1.ents:
##   print(ent._.coref_cluster)










##link = "https://www.bbc.com/news/world-europe-50740324"