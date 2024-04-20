"""
NAME
    sentilexpt
"""

import codecs

# tokenizar o HP_I em frases
import spacy
import re

from nltk.tokenize import sent_tokenize

import os
import matplotlib.pyplot as plt

__version__ = "0.0.1"

lista = []

# Boosters positivos
positive_boosters = ['muito', 'demais', 'bastante', 'mais', 'tão', 'tanto', 'quanto', 'quão' ]

# Boosters negativos
negative_boosters = ['menos', 'pouco', 'apenas', 'somente', 'quase']

# Boosters exclamação - Caso a frase seja positiva, acrescenta um, caso a frase seja negativa diminui um, caso seja neutra nao faz nada.
exclamation_boosters= ['!']

# Negadores
negation_words = ['não', 'ninguém', 'num', 'nada', 'nenhum', 'nunca', 'jamais']

# Carregar o modelo da língua portuguesa
nlp = spacy.load("pt_core_news_lg")

matcher = spacy.matcher.Matcher(nlp.vocab)

# criar dicionário sentilexpt com as palavras e respetivas polaridades
def sentiLexFlexToDict():
    fileName = "SentiLex-PT02/SentiLex-flex-PT02.txt"
    inputFile = codecs.open(fileName,"rb","utf-8")
    pt_dict = {}
    # stopwords = ['depois', 'houvesse', 'estejamos', 'tenho', 'teremos', 'houvessem', 'tiver', 'elas', 'aquele', 'nas', 'eu', 'fosse', 'estivesse', 'das', 'seus', 'até', 'qual', 'esta', 'me', 'pelos', 'ele', 'sejamos', 'éramos', 'tem', 'teve', 'estivéssemos', 'esteve', 'lhes', 'estávamos', 'tivessem', 'haver', 'entre', 'seríamos', 'lhe', 'estavam', 'terá', 'não', 'houveria', 'tínhamos', 'quando', 'mais', 'houveríamos', 'dela', 'um', 'teria', 'só', 'nos', 'esteja', 'teus', 'hei', 'o', 'essas', 'houvera', 'estas', 'forem', 'tivemos', 'seja', 'somos', 'minha', 'para', 'nosso', 'houvéramos', 'os', 'tu', 'tua', 'teu', 'hajam', 'delas', 'aqueles', 'haja', 'há', 'tivermos', 'meu', 'foram', 'houver', 'minhas', 'sejam', 'pelas', 'houveram', 'havemos', 'eles', 'for', 'meus', 'eram', 'será', 'tinha', 'ela', 'estou', 'em', 'aquilo', 'as', 'nossos', 'deles', 'estiver', 'muito', 'quem', 'temos', 'tenham', 'pela', 'pelo', 'houvermos', 'de', 'dos', 'tém', 'do', 'fui', 'foi', 'à', 'era', 'estejam', 'estiverem', 'fomos', 'nossas', 'e', 'ao', 'ou', 'seriam', 'teríamos', 'tiveram', 'seria', 'tivesse', 'fora', 'aquela', 'estamos', 'hajamos', 'estivermos', 'são', 'que', 'tive', 'ser', 'esses', 'dele', 'estivessem', 'com', 'estes', 'por', 'também', 'você', 'houvéssemos', 'tenha', 'na', 'estive', 'estar', 'estivemos', 'tivéramos', 'fossem', 'isto', 'houverão', 'te', 'seu', 'houverá', 'teriam', 'houveremos', 'sem', 'é', 'houve', 'esse', 'mesmo', 'serão', 'uma', 'numa', 'nossa', 'suas', 'hão', 'nem', 'serei', 'terei', 'isso', 'formos', 'num', 'terão', 'sua', 'houvemos', 'aquelas', 'houverei', 'da', 'este', 'estiveram', 'vocês', 'tivera', 'vos', 'houveriam', 'nós', 'está', 'estão', 'seremos', 'como', 'no', 'se', 'estivéramos', 'tuas', 'às', 'aos', 'tenhamos', 'essa', 'estivera', 'tinham', 'tivéssemos', 'a', 'fôramos', 'sou', 'mas', 'tiverem', 'fôssemos', 'já', 'houverem']
    for line in inputFile:
        pos_vir = line.find(',')
        palavra = line[:pos_vir]
        pos_pol = line.find('POL')
        polaridade = line[pos_pol+7:pos_pol+9].replace(';', '')
        pt_dict[palavra] = polaridade
    #     for stop in stopwords:
    #         if stop in palavra:
    #             print(stop)
    #             stopwords.remove(stop)
    # print(stopwords)

    # Reorder the dictionary by the number of characters in the keys in descending order
    sorted_dict = dict(sorted(pt_dict.items(), key=lambda x: len(x[0]), reverse=True))

    return sorted_dict #SentiLex-Flex em Dict
    
#print(sentiLexFlexToDict())

# Carregar o dicionário SentiLexFlex
senti_lex_dict = sentiLexFlexToDict()


def custom_sent_tokenize(text):
    # Tokenize by newline characters
    sentences = re.split(r'\n', text)
    # Further tokenize each line if it contains multiple sentences
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.extend(sent_tokenize(sentence))
    return tokenized_sentences

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
        new_sentence = re.sub(r'(?<![a-zA-Z])-|-(?![a-zA-Z])|[^\w\s\-\!]', '', sentence)
        if new_sentence != '':
            new_sentences.append(new_sentence)
    return new_sentences

def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    #return ' '.join(words)
    return words


def calculate_polarity_and_save(normalized, output_file):
    # Polaridade total do texto
    total_polarity = 0
    total_words = 0
    total_negations = 0
    total_positive_boosters = 0
    total_negative_boosters = 0
    total_positive = 0
    total_negative = 0
    # Calcular a polaridade de cada frase
    with open(output_file, 'w') as f:
        for sentence in normalized:
            doc = nlp(sentence)
            # Apply matcher on the doc
            matches = matcher(doc)
            with doc.retokenize() as retokenizer:
                for _, start, end in matches:
                    span = doc[start:end]
                    retokenizer.merge(span)
            f.write(f"{doc.text}\n")
            sentence_polarity = 0  # Inicializar a polaridade da frase
            f.write(f"Sentence: '{sentence}'\n")
            exclamation = False
            for i, token in enumerate(doc):
                if token.text in exclamation_boosters:
                    exclamation = True
                if token.text in senti_lex_dict.keys() or token.text in (positive_boosters + negative_boosters + negation_words):
                    word_polarity = 0.0  # Inicializar a polaridade da palavra
                    # verificar se é um booster positivo ou negativo e a polaridade à sua direita
                    if token.text in positive_boosters:
                        for j in range(i+1, len(doc)):
                            if doc[j].text in senti_lex_dict.keys():
                                total_positive_boosters += 1
                                # Increase the impact of positive boosters
                                word_polarity += 1.5 * float(senti_lex_dict[doc[j].text.lower()])
                    elif token.text in negative_boosters:
                        for j in range(i+1, len(doc)):
                            if doc[j].text in senti_lex_dict.keys():
                                total_negative_boosters += 1
                                # Reduce the impact of negative words
                                word_polarity += 0.5 * float(senti_lex_dict[doc[j].text.lower()])
                    elif token.text in negation_words:
                        for j in range(i+1, len(doc)):
                            if doc[j].text in senti_lex_dict.keys():
                                total_negations += 1
                                # Reduce the impact of negations
                                word_polarity += 0.5 * float(senti_lex_dict[doc[j].text.lower()])
                    elif token.text in senti_lex_dict:
                        word_polarity = int(senti_lex_dict[token.text])
                        if int(senti_lex_dict[token.text]) > 0:
                            total_positive += 1
                            # Optionally increase the value for positive words
                            word_polarity *= 1.2
                        elif int(senti_lex_dict[token.text]) < 0:
                            total_negative += 1
                            # Optionally decrease the value for negative words
                            word_polarity *= 0.8
                    sentence_polarity += word_polarity
                    total_words += 1
                    f.write(f"Polarity of the word '{token.text}': {word_polarity}\n")
            if exclamation:
                if sentence_polarity < 0:
                    sentence_polarity -= 1  # Decrease polarity further if negative
                elif sentence_polarity > 0:
                    sentence_polarity += 1  # Increase polarity further if positive
            total_polarity += sentence_polarity
            f.write(f"Sum of sentence polarity: {sentence_polarity}\n")
            if exclamation:
                f.write(" (with exclamation booster)\n")
            f.write("\n")
        f.write(f"Total Polarity: {total_polarity}\n\n")
        f.write(f"Total Words: {total_words}\n\n")
        f.write(f"Total Positive Words: {total_positive}\n")
        f.write(f"Total Negative Words: {total_negative}\n")
        f.write(f"Total Negations: {total_negations}\n")
        f.write(f"Total Positive Boosters: {total_positive_boosters}\n")
        f.write(f"Total Negative Boosters: {total_negative_boosters}\n")
        f.write("Retira as tuas ilações, oh palhaço. Não te vou dar tudo de mão beijada.")


# this function will update each output_HP polarity and save in a new folder "updated_outputHP"
def update_text_polarity(file_paths):
    # Function to extract polarity numbers from the text
    def extract_polarity(text):
        # Regular expression pattern to find polarity numbers
        pattern = r"Total Polarity: (-?\d+)"
        polarity_match = re.search(pattern, text)
        if polarity_match:
            return int(polarity_match.group(1))
        else:
            return None

    # Function to read and process each text file
    def process_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            polarity = extract_polarity(text)
            return polarity

    # Process each file and store mean polarities
    mean_polarities = []
    for i, file_path in enumerate(file_paths):  # Add 'enumerate()' to iterate over indices and values
        polarity = process_text_file(f"output/{file_path}")
        mean_polarities.append(polarity)

    # Calculate the overall mean polarity
    overall_mean_polarity = int(sum(mean_polarities) / len(mean_polarities))

    for i, file_path in enumerate(file_paths):  # Add 'enumerate()' to iterate over indices and values
        with open("updated_outputHP/updated_" + file_path, 'w', encoding='utf-8') as file:
            new_polarity = mean_polarities[i] - overall_mean_polarity
            file.write(f"Mean Polarity: {mean_polarities[i]}\n")
            file.write(f"New Polarity (with mean in zero): {new_polarity}\n")
            lista.append(new_polarity)

    return mean_polarities, lista  # Return both mean_polarities and lista

def main():
    # verificar se existe uma palavra ou frase no dicionário sentilexpt na frase tokenizada
    for palavra in senti_lex_dict.keys():
        if ' ' in palavra:
            pattern = []
            for pal in palavra.split(' '):
                pattern.append({"LOWER":pal})
            matcher.add(palavra, [pattern])

    # Criar a pasta outputHP se não existir
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista de arquivos HP
    hp_files = ['frases.txt', 'corpus/HP_I.txt', 'corpus/HP_II.txt', 'corpus/HP_III.txt', 'corpus/HP_IV.txt', 'corpus/HP_V.txt', 'corpus/HP_VI.txt', 'corpus/HP_VII.txt', 'corpus/HP_VIII.txt', 'corpus/HP_IX.txt', 'corpus/HP_X.txt', 'corpus/HP_XI.txt', 'corpus/HP_XII.txt', 'corpus/HP_XIII.txt', 'corpus/HP_XIV.txt', 'corpus/HP_XV.txt', 'corpus/HP_XVI.txt', 'corpus/HP_XVII.txt']
    # Nome dos arquivos de saída
    output_files = ['output_frases.txt', 'output_HP_I.txt', 'output_HP_II.txt', 'output_HP_III.txt', 'output_HP_IV.txt', 'output_HP_V.txt', 'output_HP_VI.txt', 'output_HP_VII.txt', 'output_HP_VIII.txt', 'output_HP_IX.txt', 'output_HP_X.txt', 'output_HP_XI.txt', 'output_HP_XII.txt', 'output_HP_XIII.txt', 'output_HP_XIV.txt', 'output_HP_XV.txt', 'output_HP_XVI.txt', 'output_HP_XVII.txt']

    # Loop sobre cada arquivo HP
    for hp_file, output_file in zip(hp_files, output_files):
        frases = custom_sent_tokenize(open(hp_file, 'r').read())
        normalized = normalize(frases)
        output_path = os.path.join(output_folder, output_file)
        calculate_polarity_and_save(normalized, output_path)
        print(f"Terminado: {output_file}")

    # Update text polarity
    mean_polarities, lista = update_text_polarity(output_files[1:])

    x = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII']

    # Plot mean_polarities
    plt.bar(x, mean_polarities)
    plt.xlabel('Capítulos')
    plt.ylabel('Polaridade de Cada Capítulo')
    plt.savefig('BarPlot_Mean_Cap.png')
    plt.clf()  # Clear current plot

    # Plot lista
    plt.bar(x, lista)
    plt.xlabel('Capítulos')
    plt.ylabel('Polaridade Com Mean a Zero')
    plt.savefig('BarPlot_With_Mean_to_Zero.png')
    plt.clf()  # Clear current plot
    
if __name__ == '__main__':
    main()