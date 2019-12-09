# python -m spacy download en

import nltk
from stat_parser import Parser  # pip3 install https://github.com/emilmont/pyStatParser/archive/master.zip
import spacy  # python -m spacy download en
from spacy import displacy
from collections import Counter
import en_core_web_sm
import webbrowser
# clone and install locally
# python setup.py install --user
# https://github.com/emilmont/pyStatParser


def tagprint(tagged):
    for word, tag in tagged:
        print(word, "("+tag+") ", end="")
    print()


def tagger(text):
    tokenized = nltk.word_tokenize(text)
    pos_tagged = nltk.pos_tag(tokenized)
    return pos_tagged

teksti = """Although Murray had privately been thinking he was approaching the end, he had given few clues publicly and that meant a tearful announcement in a pre-tournament news conference at the Australian Open surprised the world.
Murray said he thought he could get through the pain until Wimbledon and then stop playing, although he also conceded the Grand Slam in Melbourne might be his last tournament.
Yet on the morning of his planned admission he still had doubts whether he should reveal all.
"I'm going to say something today, I know I'll get emotional," he says, two hours before facing the media.
"But I change my mind all the time. I need to say something. Or I don't."
Murray describes how he is feeling nervous, anxious and has butterflies in his stomach, while walking around that morning without much pain in his hip.
"When making a decision like that I want my leg to feel really sore," he says.
That led to doubts. So he calls his physio Shane Annun. "I'm thinking I'm making a mistake," Murray says."""

teksti = ("The students like doing their exercises because they are "
          "aware of the benefits later on, especially with Finland "
          "increasing demand in job market")


if __name__ == "__main__":

    # tag the given text
    tagged = []
    for tokenized in tagger(teksti):
        tagged.append(tokenized)
    
    # create tree from given text. creates second set of tags also
    tree = Parser().parse(teksti) # this parser uses nltk
    tree.draw()
    
    # create doc from given text and get named entities from it
    nlp = en_core_web_sm.load()
    doc = nlp(teksti)
    named_entities = [(X.text, X.label_) for X in doc.ents]
    
    tagprint(tagged)
    print(tree)
    print(named_entities)
    webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s").open("http://localhost:5000")
    
    displacy.serve(doc, style='dep')
    #displacy.serve(doc, style='ent')

