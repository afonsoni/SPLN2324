import codecs

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


# tokenizar o HP_I em frases
import spacy
import re

from nltk.tokenize import sent_tokenize

def custom_sent_tokenize(text):
    # Tokenize by newline characters
    sentences = re.split(r'\n', text)
    # Further tokenize each line if it contains multiple sentences
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.extend(sent_tokenize(sentence))
    return tokenized_sentences

frases = custom_sent_tokenize(open('./corpus/HP_I.txt', 'r').read())

#frases = [
    #"Este filme é muito chato.",
    #"Eu nunca vi algo tão bonito.", #problema pk apesar de ter negador sclhr nao faz sentido alterar a polaridade
    #"Isso é menos interessante do que eu esperava.",
    #"Ele é bastante inteligente.",
    #"Nada me deixa mais feliz do que isso!", # problema
    #"O Bernardo, quando encontra um gajo feio, vai à luta!",
    #"O Bernardo, quando encontra um gajo feio, não vai à luta!",
    #"O Bernardo é muito menos feio do que o João!",
    #"O Tiago é pouco mais alto que o João!",
#]
#print(frases)

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


normalized = normalize(frases)

# print(normalized)

# verificar se existe uma palavra ou frase no dicionário sentilexpt na frase tokenizada

import spacy

# Carregar o modelo da língua portuguesa
nlp = spacy.load("pt_core_news_lg")

# Carregar o dicionário SentiLexFlex
senti_lex_dict = sentiLexFlexToDict()

matcher = spacy.matcher.Matcher(nlp.vocab)

for palavra in senti_lex_dict.keys():
    if ' ' in palavra:
        pattern = []
        for pal in palavra.split(' '):
            pattern.append({"LOWER":pal})
        matcher.add(palavra, [pattern])

# Boosters positivos
positive_boosters = ['muito', 'demais', 'bastante', 'mais', 'tão', 'tanto', 'quanto', 'quão' ]

# Boosters negativos
negative_boosters = ['menos', 'pouco', 'apenas', 'somente', 'quase']

# Boosters exclamação - Caso a frase seja positiva, acrescenta um, caso a frase seja negativa diminui um, caso seja neutra nao faz nada.
exclamation_boosters= ['!']

# Negadores
negation_words = ['não', 'ninguém', 'num', 'nada', 'nenhum', 'nunca', 'jamais']

def calculate_polarity(normalized):
    # Polaridade total do texto
    total_polarity = 0
    total_words = 0
    total_negations = 0
    total_positive_boosters = 0
    total_negative_boosters = 0
    total_positive = 0
    total_negative = 0
    # Calcular a polaridade de cada frase
    for sentence in normalized:
        doc = nlp(sentence)
        # Apply matcher on the doc
        matches = matcher(doc)
        with doc.retokenize() as retokenizer:
            for _, start, end in matches:
                span = doc[start:end]
                retokenizer.merge(span)
        print(doc.text)
        sentence_polarity = 0  # Inicializar a polaridade da frase
        print(f"Sentence: '{sentence}'")
        exclamation = False
        # stopwords = ['houvesse', 'houvessem', 'elas', 'aquele', 'eu', 'qual', 'esta', 'ele', 'lhes', 'haver', 'lhe', 'houveria', 'quando', 'houveríamos', 'dela', 'só', 'hei', 'essas', 'houvera', 'estas', 'nosso', 'houvéramos', 'tu', 'teu', 'hajam', 'delas', 'aqueles', 'haja', 'há', 'meu', 'houver', 'minhas', 'houveram', 'havemos', 'eles', 'ela', 'aquilo', 'deles', 'houvermos', 'tém', 'nossas', 'ou', 'aquela', 'hajamos', 'esses', 'dele', 'estes', 'também', 'você', 'houvéssemos', 'isto', 'houverão', 'houverá', 'houveremos', 'houve', 'esse', 'suas', 'hão', 'isso', 'houvemos', 'aquelas', 'houverei', 'este', 'vocês', 'houveriam', 'tuas', 'essa', 'já', 'houverem']
        for i, token in enumerate(doc):
            if token.text in exclamation_boosters:
                exclamation = True
            if token.text in senti_lex_dict.keys() or token.text in (positive_boosters + negative_boosters + negation_words):
                word_polarity = 0  # Inicializar a polaridade da palavra
                # verificar se é um booster positivo ou negativo e a polaridade à sua direita
                if token.text in positive_boosters:
                    for j in range(i+1,len(doc)):
                        if doc[j].text in senti_lex_dict.keys():
                            total_positive_boosters += 1
                            word_polarity += int(senti_lex_dict[doc[j].text.lower()])
                elif token.text in negative_boosters:
                    for j in range(i+1,len(doc)):
                        if doc[j].text in senti_lex_dict.keys():
                            total_negative_boosters += 1
                            word_polarity -= int(senti_lex_dict[doc[j].text.lower()])
                elif token.text in negation_words:
                    for j in range(i+1,len(doc)):
                        if doc[j].text in senti_lex_dict.keys():
                            total_negations += 1
                            word_polarity = int(senti_lex_dict[doc[j].text.lower()]) * -1
                elif token.text in senti_lex_dict:
                    word_polarity = int(senti_lex_dict[token.text])
                    if int(senti_lex_dict[token.text]) > 0:
                        total_positive += 1
                    elif int(senti_lex_dict[token.text]) < 0:
                        total_negative += 1
                sentence_polarity += word_polarity
                total_words += 1
                print(f"Polarity of the word '{token.text}': {word_polarity}")
        if exclamation:
            if sentence_polarity < 0 : sentence_polarity -= 1
            elif sentence_polarity > 0 : sentence_polarity +=1    
        total_polarity += sentence_polarity
        print(f"Sum of sentence polarity: {sentence_polarity}")
        if exclamation:
            print(" (with exclamation booster)")
        print("\n")
    print(f"Total Polarity: {total_polarity}\n")
    print(f"Total Words: {total_words}\n")
    print(contribution_to_polarity(total_positive, total_negative, total_negations, total_positive_boosters, total_negative_boosters))

def contribution_to_polarity(positive, negative, negations, positive_boosters, negative_boosters):
    print(f"Total Positive Words: {positive}\n")
    print(f"Total Negative Words: {negative}\n")
    print(f"Total Negations: {negations}\n")
    print(f"Total Positive Boosters: {positive_boosters}\n")
    print(f"Total Negative Boosters: {negative_boosters}\n")
    return "Retira as tuas ilações, oh palhaço. Não te vou dar tudo de mão beijada."


# def calculate_polarity(normalized):
#     # Polaridade total do texto
#     total_polarity = 0
#     # Calcular a polaridade de cada frase
#     for sentence in normalized:
#         doc = nlp(sentence)
#         # Apply matcher on the doc
#         matches = matcher(doc)
#         with doc.retokenize() as retokenizer:
#             for _, start, end in matches:
#                 span = doc[start:end]
#                 retokenizer.merge(span)
#         print(doc.text)
#         sentence_polarity = 0  # Inicializar a polaridade da frase
#         print(f"Sentence: '{sentence}'")

#         # Variáveis de controle para negadores e boosters
#         negation_flag = False
#         positive_booster_flag = False
#         negative_booster_flag = False
#         exclamation = False

#         for i, token in enumerate(doc):
#             word_polarity = 0  # Inicializar a polaridade da palavra
#             # Verificar se é um negador
#             if token.text in negation_words:
#                 negation_flag = True
#             # Verificar se é booster positivo
#             if token.text in positive_boosters:
#                 positive_booster_flag = True
#             # Verificar se é booster negativo
#             if token.text in negative_boosters:
#                 negative_booster_flag = True
#             # Verificar se é um exclamation
#             if token.text in exclamation_boosters:
#                 exclamation = True

#             # Caso encontre uma palavra no sintilex e tinha um negation antes inverte a polaridade dessa palavra
#             if negation_flag and token.text.lower() in senti_lex_dict:
#                 word_polarity = int(senti_lex_dict[token.text.lower()]) * -1
#                 negation_flag = False  # Reiniciar a flag após inverter a polaridade

#             # Caso encontre uma palavra no sintilex e tinha um booster positivo antes duplica a polaridade dessa palavra
#             elif positive_booster_flag and token.text.lower() in senti_lex_dict:
#                 word_polarity = int(senti_lex_dict[token.text.lower()]) * 2
#                 positive_booster_flag = False  # Reiniciar a flag após inverter a polaridade

#             # Caso encontre uma palavra no sintilex e tinha um booster negativo antes passa para metade a polaridade dessa palavra
#             elif negative_booster_flag and token.text.lower() in senti_lex_dict:
#                 word_polarity = int(senti_lex_dict[token.text.lower()] ) * 0.5
#                 negative_booster_flag = False  # Reiniciar a flag após inverter a polaridade

#             elif token.text in senti_lex_dict:
#                 word_polarity = int(senti_lex_dict[token.text])
#             sentence_polarity += word_polarity
#             print(f"Polarity of the word '{token.text}': {word_polarity}")
#         # Se houver um booster de exclamação na frase, ajustar a polaridade da frase
#         if exclamation:
#             if sentence_polarity < 0:
#                 sentence_polarity -= 1
#             elif sentence_polarity > 0:
#                 sentence_polarity += 1
#         total_polarity += sentence_polarity
#         print(f"Sum of sentence polarity: {sentence_polarity}\n")

#     print(f"Total Polarity: {total_polarity}\n")

calculate_polarity(normalized)