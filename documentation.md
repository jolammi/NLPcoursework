Example code

```python
teksti = """The students like doing their exercises because they are
aware of the benefits later on, especially with Finland increasing demand in job market"""

for i in nltk.pos_tag(nltk.word_tokenize(teksti)):print(i)
'''
('The', 'DT')
('students', 'NNS')
('like', 'IN')
('doing', 'VBG')
('their', 'PRP$')
('exercises', 'NNS')
('because', 'IN')
('they', 'PRP')
('are', 'VBP')
('aware', 'JJ')
('of', 'IN')
('the', 'DT')
('benefits', 'NNS')
('later', 'RB')
('on', 'IN')
(',', ',')
('especially', 'RB')
('with', 'IN')
('Finland', 'NNP')
('increasing', 'VBG')
('demand', 'NN')
('in', 'IN')
('job', 'NN')
('market', 'NN')
'''
```
