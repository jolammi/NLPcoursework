import nltk


def visualizer(tagged):
    for word, tag in tagged:
        print(word, "("+tag+") ", end="")
    print()


def tagger(text):
    tokenized = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokenized)
    return tagged

teksti = ("The students like doing their exercises because they are "
          "aware of the benefits later on, especially with Finland "
          "increasingdemand in job market")

if __name__ == "__main__":

    tagged = []

    for tokenized in tagger(teksti):
        tagged.append(tokenized)
    
    visualizer(tagged)
    
    
    tree = nltk.chunk.ne_chunk(tagged)
    print(tree)
    tree.draw()
    
    
    nltk.corpus.treebank_chunk