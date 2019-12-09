# python -m spacy download en

import nltk
from stat_parser import (
    Parser,
)  # pip3 install https://github.com/emilmont/pyStatParser/archive/master.zip
import spacy  # python -m spacy download en
from spacy import displacy
import en_core_web_sm
import webbrowser
from text_files import text1, text2

# clone and install locally
# python setup.py install --user
# https://github.com/emilmont/pyStatParser


def tagprint(tagged):
    for word, tag in tagged:
        print(word, "(" + tag + ") ", end="")
    print()


def tagger(text):
    tokenized = nltk.word_tokenize(text)
    pos_tagged = nltk.pos_tag(tokenized)
    return pos_tagged


if __name__ == "__main__":

    # tag the given text
    tagged = []
    for tokenized in tagger(text2):
        tagged.append(tokenized)

    # create tree from given text. creates second set of tags also

    print("ok")
    tree = Parser().parse(text2)  # this parser uses nltk
    # tree.draw()

    print("ok")

    # create doc from given text and get named entities from it
    nlp = en_core_web_sm.load()
    doc = nlp(text2)
    named_entities = [(X.text, X.label_) for X in doc.ents]

    tagprint(tagged)
    print(tree)
    print(named_entities)
    webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s").open(
        "http://localhost:5000"
    )

    displacy.serve(doc, style="dep")
    # displacy.serve(doc, style='ent')
