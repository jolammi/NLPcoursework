# NLPcoursework
A repo for the course project on course 521158S Natural Language Processing and Text Mining at University of Oulu.

It uses Python 3.7 and various libraries.

## Project assignment
Project 8. Co-referencing Textual Analysis


1.  Consider a simple co-reference example as in the following: “The students like doing their exercises because they are aware of the benefits later on, especially with Finland increasing demand in job market”. Use NLTK parser tree to identify and visualize the penn-treebank tags associated to various token of the above sentence.


2.  We are only interested in coreference resolution associated to pronoun-name association. For instance, in the above example we should be able to associate pronoun “they” to noun “student”. For this purpose, we will initially look at this coreference resolution as a matching problem. For instance, in the above example, we realize that “they” stands for plural form, so can only be associated with nouns in plural forms either in the same sentence or sentence just before it. So, one can identify all  nouns and named-entities in the sentence and check those situated before the pronoun “they”, we then assign to the pronoun to the name/named-entity that fits some commonsense reasoning (explained in subsequent tasks).


3.  For this purpose, implement an example that would allow you to identify named-entities from a given text. You can use SpaCy named-entity tagger for instance. You can inspire from implementation available at https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da.


4.  Consider the following features that you should implement in your program. The feature assigns a value for a pair of words (i, j) of the document.

    <img src="./images/table1.png" width="424" height="249"/>
    table1


5.  Implement a simple coreference resolution rule that says that if a word is a pronoun then finds the noun or named-entity of the same type (plural/singular, masculine/feminine situated on the same sentence of the pronoun but before the occurrence of the pronoun. If none is found on that sentence, then look to the previous sentence. If more than one name/named-entity matches the pronoun, then assign to the name/named-entity situated closest (in terms of number of words) to the pronoun. Make use of appropriate features in Table 1 for this reasoning.


6.  Use again the example of program provided in the link above that makes use of beautiful soup to analyze website, to perform such coreference resolution on a bbc website of your choice. Report manually the accuracy of the obtained coreference resolution and comments on the limitation of such approach.


7.  Implement the Neural Coreference resolution available at https://github.com/huggingface/neuralcoref and check the results using the same bbc website as in 6)


8.  Write down an interface that allows you to enter a website or copy and past text and generate coreference resolution output using i) the approach in 6) and ii) Neural coreference resolution.

-----------------
## Käännös parhaan ymmärryksemme mukaan

Projekti 8. Sisäviittausten (co-reference) tekstuaalinen analyysi


1.  Otetaan esimerkiksi sisäviittaukset seuraavassa lauseessa: “The students like doing their exercises because they are aware of the benefits later on, especially with Finland increasing demand in job market”. Käytä NLTK parser tree:tä tokeneihin liittyvien penn-treebank tagien tunnistamiseen ja visualisoimiseen edellisessä lauseessa.



2.  Meitä kiinnostaa vain pronominimien ja nimien välinen yhteys sisäviittausten suhteen. Esimerkiksi, ylläolevassa esimerkissä meidän pitäisi pystyä liittää pronomini "they" substantiiviin "student". Tätä tarkoitusta varten sisäviittausten ratkaisua käsitellään aluksi matching-problem:ina. Esimerkiksi ylläolevassa "they" on monikko, joten se voi liittyä monikko substanttiiviin samassa tai aiemmassa lauseessa. Joten, identifioidaan kaikki substanttiivit ja named-entityt lauseessa ja tutkitaan niitä jotka esiintyy ennen "they":tä. Tämän jälkeen liitämme pronominin named-entityyn, joka on järkeenkäypä (selitetään myöhemmin)


3.  Tätä tarkoitusta varten imolementoi esimerkki joka mahdollistaa named-entityjen tunnistamisen annetusta tekstistä. Voit käyttää SpaCy-named-entity taggeria. Voit inspiroitua implementoinnista osoitteessa:  https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da.

4. Ota huomioon seuraavat ominaisuudet jotka sinun tulee implementoida omaan ohjelmaasi. Ominaisuus antaa sanaparille (i, j) arvon dokumentissa.

    <img src="./images/table1.png" width="424" height="249"/>
    table1


5.  Implementoi yksinkertainen sisäviittausratkaisusääntö, joka kertoo onko sana pronomini vai ei, ja jos on, löytää samantyyppisen (monikko/yksikkö, femiini, maskuliininen) substantiivin tai named-entityn lauseesta kuin pronomini. Jos samasta lauseesta ei löydy yhtään, se etsii edellisestä lauseesta. Jos useampi kuin yksi nimi tai named-entity täsmää pronominiin, niin liitä lähimpänä olevaan sanoissa laskien. Käytä taulukkoa 1 (yläpuolella).


6.  Käytä edellä ollutta linkkiä, jossa käytetään bs4:ää analysoimaan valittua BBC sivua ja löytämään sisäviittaukset. Arvioi käsin ja raportoi automaattisen sisäviittausten selvittämisen tuloksia ja tarkkuutta. Kommentoi kyseisen lähestymistavan rajoitteita.


7.  Implementoi Neural Coreference resolution linkistä: https://github.com/huggingface/neuralcoref ja tsekkaa tulokset käyttäen kohdan 6 BBC sivua.


8.  Implementoi GUI, johon voi pastea linkin tai tekstiä ja generoida sisäviittaukset käyttäen kohtaa 6) ja Neural coreference resolutinia kohdasta 7)



