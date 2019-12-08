import nltk
from nltk import chunk

def visualizer(tagged):
    for word, tag in tagged:
        print(word, "("+tag+") ", end="")
    print()
    
  

teksti = ("The students like doing their exercises because they are "
          "aware of the benefits later on, especially with Finland "
          "increasingdemand in job market")

if __name__ == "__main__":

    tagged = []

    for tokenized in nltk.pos_tag(nltk.word_tokenize(teksti)):
        tagged.append(tokenized)
    
    visualizer(tagged)
    
    
    tree = chunk.ne_chunk(tagged)
    print(tree)
    tree.draw()