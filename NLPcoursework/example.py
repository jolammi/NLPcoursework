text = """
Greta Thunberg named Time Person of the Year for 2019
Greta Thunberg, the Swedish schoolgirl who inspired a global movement to fight climate change, has been named Time magazine's Person of the Year for 2019.

The 16-year-old is the youngest person to be chosen by the magazine in a tradition that started in 1927.

Speaking at a UN climate change summit in Madrid before the announcement, she urged world leaders to stop using "creative PR" to avoid real action.

The next decade would define the planet's future, she said.

Last year, the teenager started an environmental strike by missing lessons most Fridays to protest outside the Swedish parliament building. It sparked a worldwide movement that became popular with the hashtag #FridaysForFuture.

Since then, she has become a strong voice for action on climate change, inspiring millions of students to join protests around the world. Earlier this year, she was nominated as a candidate for the Nobel Peace Prize.

Who is Greta Thunberg?
Island nation's 'fight to death'
What is climate change?
Where we are in seven charts
At the UN Climate Conference in New York in September, she blasted politicians for relying on young people for answers to climate change. In a now-famous speech, she said: "You have stolen my dreams and my childhood with your empty words. We'll be watching you."

Reacting to the nomination on Twitter, the activist said: "Wow, this is unbelievable! I share this great honour with everyone in the #FridaysForFuture movement and climate activists everywhere."
Time magazine's cover for its Person of the Year edition
The teenager's message, however, has not been well received by everyone, most notably prominent conservative voices. Before her appearance in Madrid, Brazil's President Jair Bolsonaro called her a "brat" after she expressed concern about the killing of indigenous Brazilians in the Amazon.

"Greta said that the Indians died because they were defending the Amazon," Mr Bolsonaro told reporters. "It's impressive that the press is giving space to a brat like that," he said, using the Portuguese word for brat, "pirralha".

The activist responded by briefly changing her Twitter bio to "Pirralha".

She has previously been at odds with US President Donald Trump, who has questioned climate science and rolled back many US climate laws, and Russian President Vladimir Putin, who once called her a "kind but poorly informed teenager".
Announcing Time's decision on NBC, editor-in-chief Edward Felsenthal said: "She became the biggest voice on the biggest issue facing the planet this year, coming from essentially nowhere to lead a worldwide movement."

The magazine's tradition, which started as Man of the Year, recognises the person who "for better or for worse... has done the most to influence the events of the year". Last year, it named murdered and imprisoned journalists, calling them "The Guardians".

What happened in Madrid?
At the COP25 Climate Conference in Madrid, Greta Thunberg accused world powers of making constant attempts "to negotiate loopholes and to avoid raising their ambition".

"The real danger is when politicians and CEOs are making it look like real action is happening when, in fact, almost nothing is being done apart from clever accounting and creative PR," she said, drawing applause.

"In just three weeks we'll enter a new decade, a decade that will define our future," she added. "Right now, we're desperate for any sign of hope."
A speech grounded in research
This was meant to be a big moment in the talks, the elixir of the "Greta effect" bringing new energy to a flagging process. The teenager is almost certainly the most famous person here, attracting far more attention than other celebrities like Al Gore, and the UN badly needs a boost.

Her talk came over as measured, grounded in the latest research, and avoided the flash of hurt and anger she displayed in New York in September. Looking around the hall, it was striking how many of the national delegations had not turned up for this morning session at the conference.

A snub by the big fossil fuel economies? Or maybe they were too busy in the negotiations themselves?

In any event, the passion among the millions of young people who have taken to the streets to demand action on climate change feels very remote from the diplomatic struggles in these halls.

Meanwhile in Brussels, the European Commission - the EU executive - announced ambitious environmental proposals to cut the bloc's dependency on fossil fuels, hoping to make Europe carbon neutral by 2050.

Commission President Ursula von der Leyen, who took office on 1 December, called the European Green Deal Europe's "man on the Moon moment". It includes proposals that affect everything from transport and buildings to food production, and air and water pollution.

The package will be debated by EU leaders at a summit on Thursday and includes:

A €100bn (£84bn; $110bn) mechanism to help countries still heavily dependent on fossil fuels to transition to renewable energy sources
Proposals to tighten the EU's greenhouse gas emissions reduction targets for 2030
A law that will set the EU "onto an irreversible path to climate neutrality" by 2050
A plan to promote a more circular economy - a system designed to eliminate waste - that will address more sustainable products as well as a "farm to fork" strategy to improve the sustainability of food production and distribution
Reacting to the proposals, Jagoda Munic, director of environmental group Friends of the Earth Europe, said they were "too small, too few and too far off", adding: "We're on a runaway train to ecological and climate collapse and the EU Commission is gently switching gears instead of slamming on the brakes."
"""
from seapie import Seapie
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp(text)



# print(cs)
article = nlp(text)
# iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)
l = []
k = []
for X in article:
    # X = str(X)
    # Seapie()
    # if str(X)[0] in "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ":
    #     k.append([(X, X.ent_type_) ])
    print(f"{X.orth_}\t\tPOS: {X.pos_}\t\t NE type: {X.ent_type_}")

# # string = " ".join([str(x) for x in article.sents])
# # lista = [y for y in nlp(string))]
# for x in article:
#     if x.pos_ != "SPACE":
#         l.append((x.orth_,x.pos_))
#         print((x.orth_,x.pos_))

# # for i in

# print(len(k))
# print(len(l))

# from bs4 import BeautifulSoup
# import requests
# import re
# def url_to_string(url):
#     res = requests.get(url)
#     html = res.text
#     soup = BeautifulSoup(html, 'html5lib')
#     for script in soup(["script", "style", 'aside']):
#         script.extract()
#     return " ".join(re.split(r'[\n\t]+', soup.get_text()))
# # ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
# # print(ny_bb)

# len(article.ents)
# sentences = [x for x in article.sents]
# for i in range(len(sentences)):
#     print([(str(x), x.label_,x.orth_,x.pos_, x.lemma_) for x in [y
#                                         for y
#                                         in nlp(str(sentences[i]))
#                                         if not y.is_stop and y.pos_ != 'PUNCT']] + "\n")
# displacy.render(nlp(str([x for x in article.sents][20])), jupyter=True, style='ent')

