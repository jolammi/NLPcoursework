"""the purpose of this file is to parse given webpage from url, or any
given plaintext in the following way

example sentence:

  +------------[type here]-----------+
  |                                  |
  v                                  |
Olli is sleeping during the lecture. He is very tired

the relations that will be parsed are;
 +------+------------+--[type here]-----------+
 |      |            |                        |
 v      v            v                        |
noun, proper noun, named entity ... ... ...pronoun

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



class TextContainer:
    """container class for holding a single web page's or such documents
    whole text in its classified form for further processing
    """

    class SentenceContainer:
        """container class for holding a single sentences's text in its
        classified form for further processing
        """
        
        def __init__(self, sentence):
            self.doc = nlp(sentence) # the base doc
            self.nes = [(X.text, X.label_) for X in self.doc.ents] # named entities
            self.split_nes = []
            
            
            
            # here lays a dark spell of the olden times. beware.
            # split_nes contains named entities in format that stores their lenght in words, type, and starting point. this data is generated
            # by iterating over the self.doc and self.nes and then matching the correct indexes to correct named entities
            # EXAMPLE NE VS SPLIT_NE
            # [("The US White House", "PLACE"), ("First", "CARDINAL")]
            # [(("The", "US", "White", "House", "PLACE"), 10, 5), ("First", "CARDINAL", 10, 5)]
            
            self.split_nes = []
            
            for ne, ne_type in self.nes:
                for sym in """.,"_'-""":
                    if sym in ne:
                        print("possible index mismatching due to a symbol in named entity <", ne, ">")
                        
                window_size = len(ne.split(" "))
                doc_size = len(self.doc)
                
                
                
                for i in range(doc_size-window_size+1):
                    window = self.doc[i:(i+window_size)]
                    str_window = [str(tokn) for tokn in window]
                    
                    #if "Announcing Time's decision on NBC" in str(self.doc):
                    #    print(str_window)
                    #    print(ne)
                    #    input()
                    
                    
                    if " ".join(str_window) == ne:
                        if (window, ne_type, i) not in self.split_nes: # this should avoid duplication of indexes when multiples of same named entity occur
                            self.split_nes.append((window, ne_type, i))
                            continue
                
            # dark spell end
                
            self.words = {index: word_and_tag for (index, word_and_tag) in enumerate(nltk.pos_tag(nltk.word_tokenize(sentence)))} # plaintext words with indexes



    def __init__(self, plaintext):
        self.plain_sentences = [token for token in nltk.tokenize.sent_tokenize(plaintext)]
        self.sentences = {index: TextContainer.SentenceContainer(sentence) for (index, sentence) in enumerate(self.plain_sentences)}
        
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
    # link = "https://www.bbc.com/news/live/election-2019-50739883"
    link = "https://www.bbc.com/news/world-us-canada-50747374"
    
    # link = "https://www.bbc.com/news/world-asia-50741094"
    # link = "https://www.bbc.com/news/world-europe-50740324"
    
    source = parse_body_text_from_url(link)
    wholetext = TextContainer(source)



    lippu = False
    for sentence_i in wholetext.sentences.keys():
        for word_i in wholetext.sentences[sentence_i].words.keys():
            word, tag = wholetext.sentences[sentence_i].words[word_i]
            # print(sentence_i, word_i, word)
            
            
            if word in pronouns:
                lippu = True
                #print("---above was pronoun---")
                
                
            for i in wholetext.sentences[sentence_i].nes:
                if word in i:
                    #print("----above is named entity----")
                    pass
                
                
        if lippu:
            #input()
            lippu = False

            # print(wholetext.sentences[sentence_i-1].words[word_i])
    
    
    for index in wholetext.sentences.keys():
        if len(wholetext.sentences[index].nes) != len(wholetext.sentences[index].split_nes):
            print("index mismatch in sentence", index)
    
    
    
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