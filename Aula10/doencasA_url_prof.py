import requests
from bs4 import BeautifulSoup
import json
import re

main_url = 'https://www.atlasdasaude.pt/doencasAaZ/'


def get_doenca_info(url):
    info_dict = {}
    pagina_url = re.sub(r'\/doencasAaZ\/', url, main_url)
    response = requests.get(pagina_url).text
    soup = BeautifulSoup(response, 'html.parser')
    div = soup.find('div', class_='field field-name-body')
    div_html = str(div)
    desc, *sections = re.split(r'(?=<h2>)', div_html)
    for section in sections:
        soup_section = BeautifulSoup(section, 'html.parser')
        title = soup_section.h2.text
        info_dict[title] = str(soup_section)
    info_dict["desc"] = desc
    return info_dict

def extrair_doencas(html):
    doencas_dict = {}
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_="views-row")
    for div in divs:
        div_designacao = div.find("div",class_="views-field-title")
        div_descricao = div.find("div",class_="views-field-body")

        nome = div_designacao.h3.a.text
        pagina_url = div_designacao.h3.a['href']
        info_dict = get_doenca_info(pagina_url)
        descricao = div_descricao.div.text
        
        info_dict['resumo'] = descricao.strip()
        doencas_dict[nome] = info_dict

    return doencas_dict
    
final_dic = {}
main_url = 'https://www.atlasdasaude.pt/doencasAaZ/'
c = "a"
while  c <= "a":
    response = requests.get(main_url + c)
    c = chr(ord(c) + 1)
    html = response.text
    doencas_dict = extrair_doencas(html)
    final_dic = final_dic | doencas_dict


f_output = open("doencas_prof.json", "w")
json.dump(final_dic, f_output, indent=4,ensure_ascii=False)