# pip install -U spacy
# python -m spacy download pt_core_news_lg
import spacy

# Load Portuguese tokenizer, tagger, parser, and NER
nlp = spacy.load("pt_core_news_lg")

# Dictionary to map spaCy POS tags to Portuguese descriptions
pos_tags_pt = {
    "DET": "Determinante",
    "PROPN": "Nome próprio",
    "AUX": "Verbo auxiliar",
    "ADJ": "Adjetivo",
    "CCONJ": "Conjunção coordenativa",
    "ADP": "Preposição",
    "PUNCT": "Pontuação",
    "NOUN": "Substantivo",
    "VERB": "Verbo",
    "ADV": "Advérbio",
    "PRON": "Pronome",
    "NUM": "Número",
    "SCONJ": "Conjunção subordinativa",
    "X": "Outro",
}

def process_text(text):
    # Process the whole document
    doc = nlp(text)
    
    # Open the output file in write mode
    with open('output.txt', 'w') as f:
        f.write(f"| {'PALAVRAS':<23} ||| {'TIPO':<23} ||| {'LEMA ':<23}| \n")
        f.write(f"| {'-'*23} ||| {'-'*23} ||| {'-'*23}| \n")
        # Analyze syntax and named entities
        for token in doc:
            pos_pt = pos_tags_pt.get(token.pos_, token.pos_)
            f.write(f"| {token.text:<23} ||| {pos_pt:<23} ||| {token.lemma_:<23}| \n")
        
        # Find named entities, phrases, and concepts
        for entity in doc.ents:
            f.write(f"| {entity.text:<23} ||| {entity.label_:<23} ||| {entity.text:<23}| \n")

        f.write(f"| {'-'*23} ||| {'-'*23} ||| {'-'*23}| \n")

# Example text
text = ("A Universidade do Minho é uma universidade pública portuguesa, com sede em Braga e um polo em Guimarães. Está entre as melhores universidades do país.")
process_text(text)

# Analyze syntax
doc = nlp(text)  # Define the 'doc' variable
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
print("Nouns:", [token.lemma_ for token in doc if token.pos_ == "NOUN"])
print("Adjectives:", [token.lemma_ for token in doc if token.pos_ == "ADJ"])
print("Adverbs:", [token.lemma_ for token in doc if token.pos_ == "ADV"])
print("Pronouns:", [token.lemma_ for token in doc if token.pos_ == "PRON"])
print("Prepositions:", [token.lemma_ for token in doc if token.pos_ == "ADP"])
print("Conjunctions:", [token.lemma_ for token in doc if token.pos_ == "CCONJ"])
print("Determiners:", [token.lemma_ for token in doc if token.pos_ == "DET"])
print("Punctuation:", [token.lemma_ for token in doc if token.pos_ == "PUNCT"])
print("Numbers:", [token.lemma_ for token in doc if token.pos_ == "NUM"])


# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)