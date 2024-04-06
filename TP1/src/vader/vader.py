import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Função para ler os textos de um arquivo
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        textos = [line.strip() for line in file]
    return textos

# Ler os textos em português e inglês de seus respectivos arquivos
PT = read('../HP.txt')
EN = read('../HP_ingles.txt')

# Análise de sentimento em inglês
analyzer = SentimentIntensityAnalyzer()
sentimentos_ingles = [analyzer.polarity_scores(texto)["compound"] for texto in EN]

# Plotar histograma para inglês
plt.figure(figsize=(8, 6))
plt.hist(sentimentos_ingles, bins=5, color='blue', alpha=0.7)
plt.title('Histograma de Sentimento em Inglês')
plt.xlabel('Sentimento')
plt.ylabel('Frequência')
plt.savefig('histograma_ingles.png')  # Salvar o gráfico em um arquivo
plt.close()

# Análise de sentimento em português
sentimentos_portugues = [analyzer.polarity_scores(texto)["compound"] for texto in PT]

# Plotar histograma para português
plt.figure(figsize=(8, 6))
plt.hist(sentimentos_portugues, bins=5, color='red', alpha=0.7)
plt.title('Histograma de Sentimento em Português')
plt.xlabel('Sentimento')
plt.ylabel('Frequência')
plt.savefig('histograma_portugues.png')  # Salvar o gráfico em um arquivo
plt.close()
