# import spacy
# import neuralcoref

# nlp = spacy.load('en')

# # Let's try before using the conversion dictionary:
# neuralcoref.add_to_pipe(nlp)
# doc = nlp(u'Deepika has a dog. She loves him. The movie star has always been fond of animals')
# doc._.coref_clusters
# print(doc._.coref_resolved)
# output = ""
# #print(doc)

# #for i in doc._.coref_resolved:
#     #print(i)
#     #output += str(i)
#     #output += "\n"
#     #print(output)
#     #print("\n")

import spacy
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
text = 'My sister has a dog. She loves him.'
doc = nlp(text)

# print(doc._.coref_clusters)

lista = [[str(x) for x in i] for i in doc._.coref_clusters]
print(lista)

text = text.split(" ")
text2 = text.copy()
for idx, val in enumerate(text):
    for j in lista:
        # print(j)
        if j[1] in val:
            text2[idx] = text2[idx]+f" ({j[0]})"



print(" ".join(text2))


# print(type(str(doc._.coref_clusters[1].mentions)))
# print(doc._.coref_clusters[1].mentions[-1])
# print(doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main)

# token = doc[-1]
# print(token._.in_coref)
# print(token._.coref_clusters)

# span = doc[-1:]
# print(span._.is_coref)
# print(span._.coref_cluster.main)
# print(span._.coref_cluster.main._.coref_cluster)