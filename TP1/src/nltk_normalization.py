import pandas as pd
import nltk
from nltk.tokenize import WordPunctTokenizer
import re
from nltk.corpus import stopwords

# exemplo de uma frase
frase = open('HP_I.txt', 'r').read()
tokens = WordPunctTokenizer().tokenize(frase)

print(tokens)

language = 'portuguese'

#Criando a lista de stopwords
stopwords = stopwords.words(language)
stopwords = list(set(stopwords))

def remove_stopwords(words):
    """Remover as Stopwords das palavras tokenizadas"""
    new_words = []
    for word in words:
        if word not in stopwords or word == 'não':
            new_words.append(word)
    return new_words

def to_lowercase(words):
    """converter todos os caracteres para lowercase"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """remover pontuação"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return ' '.join(words)

normalized = normalize(tokens)
# print(normalized)

# Counter of negations
def count_negations(text):
    negations = ['não', 'nem', 'nada', 'ninguém', 'nenhum', 'nunca', 'jamais']
    tokens = nltk.word_tokenize(text)
    count = 0
    for token in tokens:
        if token in negations:
            count += 1
    return count

# print(count_negations(normalized))

# Counter of boosters
def count_boosters(text):
    boosters = ['muito', 'demais', 'bastante', 'mais', 'menos', 'pouco', 'tão', 'tanto', 'quanto', 'quão', 'quase', 'apenas', 'somente']
    tokens = nltk.word_tokenize(text)
    count = 0
    for token in tokens:
        if token in boosters:
            count += 1
    return count
