import os
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Função para ler o texto de um arquivo
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

# Função para ler os capítulos de uma lista de arquivos
def read_all_chapters(file_paths):
    chapters = []
    for file_path in file_paths:
        print(f"Lendo capítulo do arquivo: {file_path}")
        if os.path.exists(file_path):
            chapter_text = read(file_path)
            chapters.append(chapter_text)
        else:
            print(f"O arquivo {file_path} não foi encontrado.")
    return chapters

# Função para calcular a soma dos sentimentos de um capítulo
def calculate_sentiment_sum(text, analyzer):
    sentences = text.split('.')  # Simples segmentação de sentenças
    return sum(analyzer.polarity_scores(sentence)['compound'] for sentence in sentences if sentence)

def main():
    # Lista de caminhos para cada arquivo de capítulo
    chapter_files = [f"HP_EN/HP_EN_{roman}.txt" for roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII']]

    # Inicializar o Sentiment Intensity Analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Ler os textos de todos os capítulos
    chapters = read_all_chapters(chapter_files)

    # Verificar se o número de capítulos lidos é igual ao esperado
    if len(chapters) != len(chapter_files):
        print("Número incorreto de capítulos lidos.")
        print(f"Número de capítulos esperados: {len(chapter_files)}, Número de capítulos lidos: {len(chapters)}")
        return

    # Calcular a soma dos sentimentos para cada capítulo
    sentimentos_soma = [calculate_sentiment_sum(chapter, analyzer) for chapter in chapters]

    # Plotting the bar graph
    plt.figure(figsize=(10, 8))  # Ajusta o tamanho da figura
    plt.bar(range(1, len(sentimentos_soma)+1), sentimentos_soma, color='blue')  # Plota as barras
    plt.title('Polaridade de cada Capítulo em Inglês (Vader)')  # Título do gráfico
    plt.xlabel('Capítulos')  # Rótulo do eixo x
    plt.ylabel('Polaridade')  # Rótulo do eixo y
    plt.axhline(0, color='grey', linewidth=0.8)  # Adiciona uma linha em y=0 para referência
    plt.xticks(range(1, len(sentimentos_soma)+1),  # Configura os rótulos das marcações do eixo x para os capítulos
               ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII'])
    plt.tight_layout()  # Ajusta o gráfico para garantir que tudo se encaixe sem sobreposição
    plt.savefig('BarPlot_Vader_All_Chapters_Polarity_Sum.png')  # Salva o gráfico

if __name__ == "__main__":
    main()
