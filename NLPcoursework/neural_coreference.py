import spacy
import neuralcoref


from parse_url_to_text import parse_body_text_from_url



def neural_coreference(text):
    nlp = spacy.load('en_core_web_sm')
    neuralcoref.add_to_pipe(nlp)

    doc = nlp(text)

    output = doc._.coref_resolved
    output += "\n"

    list_of_references = str(doc._.coref_clusters)
    list_of_references =  list_of_references.replace("],", "]\n")
    list_of_references = list_of_references[1:-1]

    output += "\n------- Named entities and their reference pronouns -------\n\n"
    output += list_of_references

    return output

if __name__ == "__main__":
    link = "https://www.bbc.com/news/world-europe-50740324"
    doc1 = parse_body_text_from_url(link)
    output = neural_coreference(doc1)
    print(output)
