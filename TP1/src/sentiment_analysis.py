import pandas as pd

sentilexpt = open("SentiLex-PT02/SentiLex-lem-PT02.txt", "r", encoding = "utf-8")

# Create a dictionary with the words and their polarities
dic_palavra_polaridade = {}

for i in sentilexpt.readlines():
    pos_pon = i.find('.')
    palavra = (i[:pos_pon])
    pos_pol = i.find('POL')
    polaridade = (i[pos_pol+7:pos_pol+9]).replace(';','')
    dic_palavra_polaridade[palavra] = polaridade

print(dic_palavra_polaridade)

# sentilex_database = pd.read_csv("SentiLex-PT02/SentiLex-flex-PT02.txt",header = None)
# print(sentilex_database)
# sentilex_database.columns = ["adjective", "description"]
# # extract "polarity" from "description"
# polarity = pd.DataFrame(sentilex_database.description.str.split("\;+").str[3].str.split("\=+").str[1])
# sentilex_database = pd.concat([sentilex_database, polarity],axis = 1, join = "outer")
# # remove duplicates
# sentilex_database = sentilex_database.iloc[:, [0, 2]].drop_duplicates()
# sentilex_database.columns = ["adjective", "polarity"]
# # select only polarities in [-1, 0, 1]
# polarities = ["-1", "0", "1"]
# sentilex_database = sentilex_database[sentilex_database.polarity.isin(polarities)]

# print(sentilex_database.head())

# Function to calculate the polarity of a sentence
# def polaridade_frase(frase):
#     polaridade = 0
#     for palavra in frase.split():
#         if palavra in dic_palavra_polaridade:
#             polaridade += int(dic_palavra_polaridade[palavra])
#     return polaridade

# # Example sentences
# frase1 = "Eu gosto muito de estudar."
# frase2 = "Eu odeio matemática."
# frase3 = "Eu não gosto de estudar."

# print(f"Polaridade da frase '{frase1}': {polaridade_frase(frase1)}")
# print(f"Polaridade da frase '{frase2}': {polaridade_frase(frase2)}")
# print(f"Polaridade da frase '{frase3}': {polaridade_frase(frase3)}")
