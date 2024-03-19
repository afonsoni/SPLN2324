#!/usr/bin/env python3
'''
NAME
    word_freq - Calculates word frequency in a text

SYNOPSIS
    word_freq [options] input_files
    options: 
        -m 20 - Show the 20 most common words
		-n : Order alphabetically
		-i 1 : Order by number of appearances

Description
'''

from collections import Counter
from jjcli import *
import re

cl = clfilter("nmi:", doc=__doc__) # option values in cl.opt dictionary

def tokeniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[.,;:_!?—]+', texto)
    return palavras

def imprimeN(lista, file):
    file.write("Occurrences\tWord\n")
    for palavra, n_ocorr in lista:
        file.write(f"{n_ocorr}\t{palavra}\n")
        print(f"{n_ocorr}\t{palavra}")

def imprimeM(lista, file):
    file.write("Word\tOccurrences\n")
    for palavra, n_ocorr in lista:
        file.write(f"{n_ocorr}\t{palavra}\n")
        print(f"{n_ocorr}\t{palavra}")

def imprimeI(lista, file):
    lista = list(lista)
    lista.sort(key=lambda x: (-x[1], x[0]))
    file.write("Word\tOccurrences\n")
    for palavra, n_ocorr in lista:
        file.write(f"{palavra}\t{n_ocorr}\n")


try:
    with open('output.txt', 'w') as file:
        for txt in cl.text(): # process one file at a time
            listas_palavras = tokeniza(txt)
            if "-m" in cl.opt:
                ocorr = Counter(listas_palavras)
                imprimeM(ocorr.most_common(int(cl.opt.get("-m"))), file)
            elif "-n" in cl.opt:
                listas_palavras.sort()
                ocorr = Counter(listas_palavras)
                imprimeN(ocorr.items(), file)
            elif "-i" in cl.opt:
                ocorr = Counter(listas_palavras)
                imprimeI(ocorr.items(), file)
            else:
                print("Erro ao correr!")
except Exception as e:
    print(f"Error: {e}")
