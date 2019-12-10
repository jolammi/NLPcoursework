import nltk
import spacy
import webbrowser
import en_core_web_sm
from spacy import displacy
from stat_parser import Parser
from text_files import text1, text2


# installation notes for libraries
#
# clone and install pystatparser locally:
# python setup.py install --user
# https://github.com/emilmont/pyStatParser
# or use the following
# pip3 install https://github.com/emilmont/pyStatParser/archive/master.zip
#
# import spacy  # use following for library: python -m spacy download en

def tagger(text):
    tokenized = nltk.word_tokenize(text)
    pos_tagged = nltk.pos_tag(tokenized)
    return pos_tagged


if __name__ == "__main__":
    nlp = en_core_web_sm.load()
    source = text2
    sentences = [source] # TODO: logiikka että saadaan N lauseen lista

    for sentence in sentences:
        tagged = [tokenized for tokenized in tagger(source)]
        tree = Parser().parse(source)
        doc = nlp(source)
        named_entities = [(X.text, X.label_) for X in doc.ents]
        
        # show tree structure in tkinter window for the sentence
        tree.draw()
        
        # print tagged text in flat format
        for word, tag in tagged: print(word, "(" + tag + ") ", end="")
        
        # print tagged text in tree format (different tags than above!)
        print(tree)
        
        # dump named entities from the sentence
        print(named_entities)
        
        # visualize connections between words in the sentence in browser
        browser = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
        webbrowser.get(browser).open("http://localhost:5000")
        displacy.serve(doc, style="dep") # or style="ent"
