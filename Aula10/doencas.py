import requests
import json
from bs4 import BeautifulSoup

open('doencas.json', 'w').close()


for letter in range(ord('a'), ord('z')+1):
    url = requests.get(f'https://www.atlasdasaude.pt/doencasAaZ/{chr(letter)}')

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

    with open('doencas.json', 'a') as f_out:
        if letter == ord('a'):
            f_out.write('[\n')
        json.dump(doencas, f_out, indent=4, ensure_ascii=False)
        if letter != ord('z'):
            f_out.write(',\n')
        else:
            f_out.write('\n]')