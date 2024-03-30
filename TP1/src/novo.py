import codecs

# criar dicionário sentilexpt com as palavras e respetivas polaridades
def sentiLexFlexToDict():
    fileName = "SentiLex-PT02/SentiLex-flex-PT02.txt"
    inputFile = codecs.open(fileName,"rb","utf-8")
    pt_dict = {}
    for line in inputFile:
        pos_vir = line.find(',')
        palavra = line[:pos_vir]
        pos_pol = line.find('POL')
        polaridade = line[pos_pol+7:pos_pol+9].replace(';', '')
        pt_dict[palavra] = polaridade
    
    # Reorder the dictionary by the number of characters in the keys in descending order
    sorted_dict = dict(sorted(pt_dict.items(), key=lambda x: len(x[0]), reverse=True))

    return sorted_dict #SentiLex-Flex em Dict
    
# print(sentiLexFlexToDict())


# tokenizar o HP_I em frases
import nltk
from nltk.tokenize import sent_tokenize
import re

def custom_sent_tokenize(text):
    # Tokenize by newline characters
    sentences = re.split(r'\n', text)
    # Further tokenize each line if it contains multiple sentences
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.extend(nltk.sent_tokenize(sentence))
    return tokenized_sentences

frases = custom_sent_tokenize(open('./corpus/HP_I.txt', 'r').read())

print(frases)

def to_lowercase(sentences):
    """converter todos os caracteres para lowercase"""
    new_sentences = []
    for sentence in sentences:
        new_sentence = sentence.lower()
        new_sentences.append(new_sentence)
    return new_sentences

# não remover pontos de exclamação? Tornar frases exclamativas como boosters? "Boa ideia, Joana!" (exemplo de booster)
def remove_punctuation(sentences):
    """remover pontuação"""
    new_sentences = []
    for sentence in sentences:
        new_sentence = re.sub(r'[^\w\s]', '', sentence)
        if new_sentence != '':
            new_sentences.append(new_sentence)
    return new_sentences

def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    return ' '.join(words)

normalized = normalize(frases)
#print(normalized)

# verificar se existe uma palavra ou frase no dicionário sentilexpt na frase tokenizada

