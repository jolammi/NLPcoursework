from stat_parser import Parser
import nltk
import spacy
import webbrowser
from spacy import displacy
from stat_parser import Parser
from text_files import short_text
import en_core_web_sm; nlp = en_core_web_sm.load() # second part is deemed import-like

short_text = (
    "The students like doing their exercises because they are "
    "aware of the benefits later on, especially with Finland "
    "increasing demand in job market."
)

sentences = [short_text]
for index, sentence in enumerate(sentences):

    tree = Parser().parse(sentence)
    doc = nlp(sentence)
    print("=====", "parsing sentence", index+1, "of", len(sentences), "=====")

    tagged = [tokenized for tokenized in nltk.pos_tag(nltk.word_tokenize(sentence))]
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
    # browser = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    # print("ctrl+c to continue by closing the server")
    # webbrowser.get(browser).open("http://localhost:5000")
    try:
        displacy.serve(doc, style="ent") # or style="ent" or style="dep"
    except KeyboardInterrupt:
        pass # allow breaking the server quickly
    print("=====", "server closed. finished parsing:", index+1, "of", len(sentences), "=====")