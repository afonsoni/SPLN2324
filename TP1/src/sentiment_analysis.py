###Part I - elaboration of the dictionary of words taken from the news###

import nltk
from nltk.corpus import PlaintextCorpusReader

#loading corpus words to generate dictionary
corpus_root = "./corpus/"
wordlists = PlaintextCorpusReader(corpus_root, '.*')
texto = wordlists.words()
palavrasDistintas = set(texto)

#generating stopwords list
from nltk.corpus import stopwords
from unicodedata import normalize
from nltk.tokenize import WordPunctTokenizer
portugues_stops = set(stopwords.words('portuguese'))

portugues_stop2 = ''
for word in portugues_stops:
    normalized_word = normalize('NFKD', word).encode('ASCII', 'ignore').decode('utf-8')
    portugues_stop2 = portugues_stop2 + ' ' + normalized_word

tokenizer = WordPunctTokenizer()
portugues_stop3 = tokenizer.tokenize(portugues_stop2)
var_file = open("stopwords.txt", "a")
for word in portugues_stop3:
	var_file.write(word.lower()+'\n')
var_file.close()

#removing stopwords from the dictionary
palavrasSemStop = [word.lower() for word in palavrasDistintas if word.lower() not in portugues_stop3]

#removing numbers from the list
lista = []
for word in palavrasSemStop:
	for i in range(10):
		if (word.startswith(str(i))) or (word.endswith(str(i))) or (str(i) in word):
			lista.append(word)

palavrasSemNumero = [word.lower() for word in palavrasSemStop if word.lower() not in lista]

#removing symbols and special characters
import re
palavrasSemSimbolos = [w for w in palavrasSemNumero if re.search('^[a-z]+$', w)]

#removing words with less than 3 characters
palavrasFinal = sorted([w for w in set(palavrasSemSimbolos) if len(w) >= 3])

#saving the dictionary of words
var_file = open("dicionario_corpus.txt", "a")
for word in palavrasFinal:
	var_file.write(word.lower()+'\n')

var_file.close()
