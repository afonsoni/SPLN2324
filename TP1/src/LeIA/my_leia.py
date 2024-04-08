import os
import matplotlib.pyplot as plt
from leia import SentimentIntensityAnalyzer

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

def main():
    # Lista de caminhos para cada arquivo de capítulo
    chapter_files = [f"corpus/HP_{roman}.txt" for roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII']]

    # Inicializar o Sentiment Intensity Analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Ler os textos de todos os capítulos
    chapters = read_all_chapters(chapter_files)

    # Verificar se o número de capítulos lidos é igual ao esperado
    if len(chapters) != len(chapter_files):
        print("Número incorreto de capítulos lidos.")
        print(f"Número de capítulos esperados: {len(chapter_files)}, Número de capítulos lidos: {len(chapters)}")
        return

    # Análise de sentimento para todos os capítulos
    sentimentos_ingles = [analyzer.polarity_scores(chapter)['compound'] for chapter in chapters]

    # Plotar gráfico de barras para a polaridade de todos os capítulos
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(sentimentos_ingles)+1), sentimentos_ingles, color='blue', alpha=0.7)
    plt.title('Polaridade de cada Capítulo (LeIA)')
    plt.xlabel('Capítulo')
    plt.ylabel('Polaridade')
    plt.xticks(range(1, len(chapter_files)+1), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII'])
    plt.savefig('BarPlot_LeIA_All_Chapters_Polarity.png') 

if __name__ == "__main__":
    main()
