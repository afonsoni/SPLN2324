import requests
import json
from bs4 import BeautifulSoup

url = requests.get('https://www.atlasdasaude.pt/doencasAaZ')

soup = BeautifulSoup(url.text, 'html.parser')

doencas = {}

# Isto é parvo
# for doenca in soup.find_all('div', class_='views-field views-field-title'):
#     nome = doenca.find('h3').text
#     for doenca in soup.find_all('div', class_='field-content'):
#         descricao_tag = doenca.find('p')
#         if descricao_tag is not None:
#             descricao = descricao_tag.text
#             doencas[nome] = descricao

divs = soup.find_all('div', class_='views-row')
for div in divs:
    div_title = div.find('div', class_='views-field-title')
    div_body = div.find('div', class_='views-field-body')
    title = div_title.h3.a.text
    if div_body.div.p is not None:
        body = div_body.div.p.text 
    else: 
        body = div_body.div.div.text
    doencas[title] = body

print(doencas)

f_out = open('doencasA.json', 'w')
json.dump(doencas, f_out, indent=4, ensure_ascii=False)