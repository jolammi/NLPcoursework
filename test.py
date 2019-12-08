# python -m spacy download en

import nltk
from stat_parser import Parser

# clone and install locally
# python setup.py install --user
# https://github.com/emilmont/pyStatParser


def visualizer(tagged):
    for word, tag in tagged:
        print(word, "("+tag+") ", end="")
    print()


def tagger(text):
    tokenized = nltk.word_tokenize(text)
    pos_tagged = nltk.pos_tag(tokenized)
    return pos_tagged


teksti = ("The students like doing their exercises because they are "
          "aware of the benefits later on, especially with Finland "
          "increasing demand in job market")

if __name__ == "__main__":

    tagged = []
    for tokenized in tagger(teksti):
        tagged.append(tokenized)
    visualizer(tagged)
    
    parser = Parser()
    tree = parser.parse(teksti)
    tree.draw()
    print(tree)
