import requests
from bs4 import BeautifulSoup
import json

def extrair_doencas(html):

    doencas = {}

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_="views-row")
    for div in divs:
        div_designacao = div.find("div",class_="views-field-title")
        div_descricao = div.find("div",class_="views-field-body")

        nome = div_designacao.h3.a.text

        if div_descricao.div.p is not None:
            descricao = div_descricao.div.p.text

        else: descricao = div_descricao.div.div.text

        doencas[nome] = descricao.strip()
    return doencas
    
final_dic = {}
main_url = 'https://www.atlasdasaude.pt/doencasAaZ/'
c = "a"
while  c <= "z":
    response = requests.get(main_url + c)
    c = chr(ord(c) + 1)
    html = response.text
    doencas_dict = extrair_doencas(html)
    final_dic = final_dic | doencas_dict


f_output = open("doencas_prof.json", "w")
json.dump(final_dic, f_output, indent=4,ensure_ascii=False)