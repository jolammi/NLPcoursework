import spacy
import neuralcoref

nlp = spacy.load('en')

# Let's try before using the conversion dictionary:
neuralcoref.add_to_pipe(nlp)
doc = nlp(u'Deepika has a dog. She loves him. The movie star has always been fond of animals')
doc._.coref_clusters
print(doc._.coref_resolved)
output = ""
#print(doc)

#for i in doc._.coref_resolved:
    #print(i)
    #output += str(i)
    #output += "\n"
    #print(output)
    #print("\n")