## In case If you have an error mentioning spacy.strings.StringStore size changed, may indicate binary incompatibility
## pip3 uninstall neuralcoref
## pip3 uninstall spacy
## pip3 install spacy==2.1.6
## pip3 install --upgrade setuptools
## pip3 install cython==0.29.14
## pip3 install https://github.com/huggingface/neuralcoref/archive/master.zip
## python -m spacy download en

## Ehkä merkitystä numpy==1.17.2

##check this out
##https://huggingface.co/coref/?text=Students%20are%20hungry%20but%20they%20feel%20the%20need%20for%20speed.


import spacy
import neuralcoref

from parse_url_to_text import parse_body_text_from_url




nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
link = "https://www.bbc.com/news/world-europe-50740324"
##doc1 = "Students are hungry but they feel the need for speed."
##doc1 = "Students are hungry but they feel the need for speed. Students really like John. John is a sick bastard and he is white."
##doc1 = "The 16-year-old is the youngest person to be chosen by the magazine in a tradition that started in 1927. Speaking at a UN climate change summit in Madrid before the announcement, she urged world leaders to stop using creative PR to avoid real action. The next decade would define the planet's future, she said. Last year, the teenager started an environmental strike by missing lessons most Fridays to protest outside the Swedish parliament building. It sparked a worldwide movement that became popular with the hashtag #FridaysForFuture. Since then, she has become a strong voice for action on climate change, inspiring millions of students to join protests around the world. Earlier this year, she was nominated as a candidate for the Nobel Peace Prize."
doc1 = parse_body_text_from_url(link)
doc1 = nlp(doc1)
##print(doc1)
print(doc1._.coref_clusters)  ##All the clusters of corefering mentions in the doc


##for ent in doc1.ents:
##   print(ent._.coref_cluster)










##link = "https://www.bbc.com/news/world-europe-50740324"