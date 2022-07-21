import requests
from bs4 import BeautifulSoup

from scrapper.utils import get_text_in_li

def run_scrapper():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    endereco_da_pagina = "https://ru.ufrn.br/"
    objeto_response = requests.get(endereco_da_pagina, headers=headers)
    pagina_bs = BeautifulSoup(objeto_response.content, 'html.parser')
    return pagina_bs

def get_almoco():
    pagina_bs = run_scrapper()
    div_almoco = pagina_bs.find_all("li", {"class": "Almoço"})
    almoco_nonvegan = []
    almoco_nonvegan.append(get_text_in_li(div_almoco[0]))
    almoco_nonvegan.append(get_text_in_li(div_almoco[1]))
    almoco_vegan = []
    almoco_vegan.append(get_text_in_li(div_almoco[2]))
    return almoco_nonvegan, almoco_vegan

def get_janta():
    pagina_bs = run_scrapper()
    div_janta = pagina_bs.find_all("li", {"class": "Janta"})
    janta_nonvegan = []
    janta_nonvegan.append(get_text_in_li(div_janta[0]))
    janta_nonvegan.append(get_text_in_li(div_janta[1]))
    janta_vegan = []
    janta_vegan.append(get_text_in_li(div_janta[2]))
    return janta_nonvegan, janta_vegan

def get_cardapio():
    pagina_bs = run_scrapper()
    div_almoco = pagina_bs.find_all("li", {"class": "Almoço"})
    almoco_nonvegan = []
    almoco_nonvegan.append(get_text_in_li(div_almoco[0]))
    almoco_nonvegan.append(get_text_in_li(div_almoco[1]))
    almoco_vegan = []
    almoco_vegan.append(get_text_in_li(div_almoco[2]))
    div_janta = pagina_bs.find_all("li", {"class": "Janta"})
    janta_nonvegan = []
    janta_nonvegan.append(get_text_in_li(div_janta[0]))
    janta_nonvegan.append(get_text_in_li(div_janta[1]))
    janta_vegan = []
    janta_vegan.append(get_text_in_li(div_janta[2]))
    return almoco_nonvegan, almoco_vegan, janta_nonvegan, janta_vegan

