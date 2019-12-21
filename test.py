"""the purpose of this file is to parse given webpage from url, or any
given plaintext in the following way

example sentence:

  +------------[type here]-----------+
  |                                  |
  v                                  |
Olli is sleeping during the lecture. He is very tired

the relations that will be parsed are;
 +--------------------+------------+--[type here]-----------+
 |                    |            |                        |
 v                    v            v                        |
noun(substantive), proper noun, named entity ... ... ...pronoun

"""

try:
    from seapie import Seapie as seapie # DEBUG
except:
    print("do pip3 install seapie. importerror happened")

import nltk
import spacy
import webbrowser
from spacy import displacy
from pronouns import pronouns
from stat_parser import Parser
from parse_url_to_text import parse_body_text_from_url
from text_files import long_text, short_text, pronoun_text
import en_core_web_sm; nlp = en_core_web_sm.load() # second part is deemed import-like

# installation notes for libraries
#
# clone and install pystatparser locally:
# python setup.py install --user
# https://github.com/emilmont/pyStatParser
# or use the following
# pip3 install https://github.com/emilmont/pyStatParser/archive/master.zip
#
# import spacy  # use following for library: python -m spacy download en



def pprint(text):
    for idx, chr in enumerate('"' + text + '"'):
            print(chr, end="")
            if idx % 79 == 0 and idx != 0:
                print()
    print()



def neprint(text, ne_indexes):
    accumulator = []
    starts = []
    stops = []
    
    for start, stop in ne_indexes:
        starts.append(start)
        stops.append(stop)

    accumulator = []

    for idx, chr in enumerate(text):

            if idx in starts:
                accumulator.append("◄")

            if idx in stops:
                accumulator.append("►")
                
            accumulator.append(chr)
                
    for idx, chr in enumerate('"' + "".join(accumulator) + '"'):
        print(chr, end="")
        if idx % 79 == 0 and idx != 0:
            print()
    print()

def pronounprint(postags):
    accumulator = []
    for word, tag in postags:
        if tag in ["PRP", "PRP$", "WP$", "WP"]:
            accumulator.append("◄" + word + "►")
        else:
            accumulator.append(word)

    for idx, chr in enumerate('"' + " ".join(accumulator) + '"'):
        print(chr, end="")
        if idx % 79 == 0 and idx != 0:
            print()
    print()

class TextContainer:
    """container class for holding a single web page's or such documents
    whole text in its classified form for further processing
    """

    class SentenceContainer:
        """container class for holding a single sentences's text in its
        classified form for further processing
        """
        
        def __init__(self, sentence):
            self.txt = sentence
            self.doc = nlp(sentence) # the nlp base doc
            self.nes = [(X.text, X.label_) for X in self.doc.ents] # named entities
            self.pos = [token for token in nltk.pos_tag(nltk.word_tokenize(sentence))]
            
            self.ne_indexes = []
            self.noun_indexes = []
            self.pronoun_indexes = []
            self.propernoun_indexes = []

            
            ## THIS BLOCK WILL CREATE NAMED ENTITY INDEXES
            for ne, ne_type in self.nes:
                index = sentence.find(ne) # find first index of occurence. will be -1 if nonexistent
                while index != -1:   # while occurence exists
                    index = sentence.find(ne, index) # find new index for it
                    if index != -1: # if result is that something exists
                        if not (index, index+len(ne)) in self.ne_indexes: # and is not already listed
                            self.ne_indexes.append((index, index+len(ne))) # add it to the list
                        index += 1 # and increase count by 1 to find next one
            # this will result in the following error:
            # "Europe" is matched from "European comission" if both "Europe" and "European comission" are in the sentence
            # resulting in two matches of "Europe"
            # the following clears it
            duplicates = []
            for start, end in self.ne_indexes:
                for start2, end2 in self.ne_indexes:
                    if start2 >= start and end2 <= end:
                        if not (start == start2 and end == end2):
                            duplicates.append((start2, end2))
            for i in duplicates:
                self.ne_indexes.remove(i)


            ## THIS BLOCK WILL CREATE PRONOUN INDEXES. ITS ALMOST COPYPASTE OF BELOW BLOCK
            for pos, pos_type in self.pos:
                if pos_type in ["PRP", "PRP$", "WP$", "WP"]:
                    index = sentence.find(pos) # find first index of occurence. will be -1 if nonexistent
                    while index != -1:   # while occurence exists
                        index = sentence.find(pos, index) # find new index for it
                        if index != -1: # if result is that something exists
                            if not (index, index+len(pos)) in self.pronoun_indexes: # and is not already listed
                                self.pronoun_indexes.append((index, index+len(pos))) # add it to the list
                            index += 1 # and increase count by 1 to find next one
                # this will result in the following error:
                # "Europe" is matched from "European comission" if both "Europe" and "European comission" are in the sentence
                # resulting in two matches of "Europe"
                # the following clears it
                duplicates = []
                for start, end in self.pronoun_indexes:
                    for start2, end2 in self.pronoun_indexes:
                        if start2 >= start and end2 <= end:
                            if not (start == start2 and end == end2):
                                duplicates.append((start2, end2))
                for i in duplicates:
                    self.pronoun_indexes.remove(i)
            
            
            ## THIS BLOCK WILL CREATE PROPER NOUN INDEXES. ITS ALMOST COPYPASTE OF BELOW BLOCK
            for pos, pos_type in self.pos:
                if pos_type in ["NNP", "NNPS"]:
                    index = sentence.find(pos) # find first index of occurence. will be -1 if nonexistent
                    while index != -1:   # while occurence exists
                        index = sentence.find(pos, index) # find new index for it
                        if index != -1: # if result is that something exists
                            if not (index, index+len(pos)) in self.propernoun_indexes: # and is not already listed
                                self.propernoun_indexes.append((index, index+len(pos))) # add it to the list
                            index += 1 # and increase count by 1 to find next one
                # this will result in the following error:
                # "Europe" is matched from "European comission" if both "Europe" and "European comission" are in the sentence
                # resulting in two matches of "Europe"
                # the following clears it
                duplicates = []
                for start, end in self.propernoun_indexes:
                    for start2, end2 in self.propernoun_indexes:
                        if start2 >= start and end2 <= end:
                            if not (start == start2 and end == end2):
                                duplicates.append((start2, end2))
                for i in duplicates:
                    self.propernoun_indexes.remove(i)


            ## THIS BLOCK WILL CREATE PROPER NOUN INDEXES. ITS ALMOST COPYPASTE OF ABOVE BLOCK
            for pos, pos_type in self.pos:
                if pos_type in ["NNS", "NN"]:
                    index = sentence.find(pos) # find first index of occurence. will be -1 if nonexistent
                    while index != -1:   # while occurence exists
                        index = sentence.find(pos, index) # find new index for it
                        if index != -1: # if result is that something exists
                            if not (index, index+len(pos)) in self.noun_indexes: # and is not already listed
                                self.noun_indexes.append((index, index+len(pos))) # add it to the list
                            index += 1 # and increase count by 1 to find next one
                # this will result in the following error:
                # "Europe" is matched from "European comission" if both "Europe" and "European comission" are in the sentence
                # resulting in two matches of "Europe"
                # the following clears it
                duplicates = []
                for start, end in self.noun_indexes:
                    for start2, end2 in self.noun_indexes:
                        if start2 >= start and end2 <= end:
                            if not (start == start2 and end == end2):
                                duplicates.append((start2, end2))
                for i in duplicates:
                    self.noun_indexes.remove(i)



    def __init__(self, plaintext):
        # self.plain_sentences = [token for token in nltk.tokenize.sent_tokenize(plaintext)]
        # self.sentences = {index: TextContainer.SentenceContainer(sentence) for (index, sentence) in enumerate(self.plain_sentences)}
        self.sentences = [TextContainer.SentenceContainer(sentence) for sentence in nltk.tokenize.sent_tokenize(plaintext)]
        
        self.connections = []
        # from TextContainer index, from SentenceContainer index
        # to TextContainer index, to SentenceContainer index
        #
        # example: the word "He" should point to "Jouni" in the below sentence:
        # "Jouni has a headache. He thusly ingested 50mg theanine and 200mg caffeine"
        # this is saved as [ ... , ((1, 0), (0, 0)) , ...] which stands for
        # pointing from first word of second sentence to first word of first sentence.



if __name__ == "__main__":
    # source = pronoun_text
    # link = "https://www.bbc.com/news/world-asia-50723352"
    # link = "https://www.bbc.com/news/world-us-canada-50747374"
    # link = "https://www.bbc.com/news/world-asia-50741094"
    link = "https://www.bbc.com/news/world-europe-50740324"
    # link = "https://www.bbc.com/news/live/election-2019-50739883" # erittäin vaikea
    

    source = parse_body_text_from_url(link)
    wholetext = TextContainer(source)

    for index, sentence in enumerate(wholetext.sentences):
        if len(sentence.nes) != len(sentence.ne_indexes):
            print("index mismatch in sentence", index)
            exit()
        
        print("─"*80)
        print("SENTENCE INDEX:", index)
        
        print("\nPLAINTEXT")
        pprint(sentence.txt)
        
        print("\n◄NAMED ENTITIES►")
        neprint(sentence.txt, sentence.ne_indexes)
        
        print("\n◄PRONOUNS►")
        pronounprint(sentence.pos)
        
        
        # for start, end in sentence.ne_indexes:
        #     print(sentence.txt[start:end])
            
        input()
        
        
        for sentence in wholetext.sentences:
            sentence.pos
        
    seapie()

    
    # for index, sentence in enumerate(sentences):

        # print("======")
        # print(named_entities)
        
        # seapie()
        
        # =========== OLD MAIN BLOCK BEGIN. DO NOT REMOVE ===========
        # =========== OLD MAIN BLOCK BEGIN. DO NOT REMOVE ===========
        # =========== OLD MAIN BLOCK BEGIN. DO NOT REMOVE ===========
        # print("=====", "parsing sentence", index+1, "of", len(sentences), "=====")
        
        # tagged = [tokenized for tokenized in nltk.pos_tag(nltk.word_tokenize(sentence))]
        # tree = Parser().parse(sentence)
        # doc = nlp(sentence)
        # named_entities = [(X.text, X.label_) for X in doc.ents]
        
        # show tree structure in tkinter window for the sentence
        # tree.draw()
        
        # print tagged text in flat format
        # for word, tag in tagged: print(word, "(" + tag + ") ", end="")
        
        # print tagged text in tree format (different tags than above!)
        # print(tree)
        
        # dump named entities from the sentence
        # print(named_entities)
        
        # visualize connections between words in the sentence in browser
        # browser = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
        # print("ctrl+c to continue by closing the server")
        # webbrowser.get(browser).open("http://localhost:5000")
        # try:
        #     displacy.serve(doc, style="ent") # or style="ent" or style="dep"
        # except KeyboardInterrupt:
        #     pass # allow breaking the server quickly
        # print("=====", "server closed. finished parsing:", index+1, "of", len(sentences), "=====")
        # =========== OLD MAIN BLOCK END DO NOT REMOVE ===========
        # =========== OLD MAIN BLOCK END DO NOT REMOVE ===========
        # =========== OLD MAIN BLOCK END DO NOT REMOVE ===========




"""
penn-treebank tag explanations

CC    Coordinating conjunction
CD    Cardinal number
DT    Determiner
EX    Existential there
FW    Foreign word
IN    Preposition or subordinating conjunction
JJ    Adjective
JJR   Adjective, comparative
JJS   Adjective, superlative
LS    List item marker
MD    Modal
NN    Noun, singular or mass
NNS   Noun, plural
NNP   Proper noun, singular
NNPS  Proper noun, plural
PDT   Predeterminer
POS   Possessive ending
PRP   Personal pronoun
PRP$  Possessive pronoun
RB    Adverb
RBR   Adverb, comparative
RBS   Adverb, superlative
RP    Particle
SYM   Symbol
TO    to
UH    Interjection
VB    Verb, base form
VBD   Verb, past tense
VBG   Verb, gerund or present participle
VBN   Verb, past participle
VBP   Verb, non-3rd person singular present
VBZ   Verb, 3rd person singular present
WDT   Wh-determiner
WP    Wh-pronoun
WP$   Possessive wh-pronoun
WRB   Wh-adverb
"""


"""
tags found so far
NN
IN
CD
RBR
JJR
RB
VBZ
MD
VBN
JJ
VB
JJS
PRP
WP
UH
NNS
VBD
RBS
VBG
WDT
$
VBP
NNPS
NNP
TO
POS
DT
RP
PRP$
WRB
CC
"""