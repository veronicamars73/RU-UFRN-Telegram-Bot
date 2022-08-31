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
    div_principal = (pagina_bs.find_all("div", {"class": "proteinas"})[0].find("li", {"class": "Almoço"}))
    div_acomp = (pagina_bs.find_all("div", {"class": "acompanhamentos"})[0].find("li", {"class": "Almoço"}))
    div_vegan = (pagina_bs.find_all("div", {"class": "vegetariano"})[0].find("li", {"class": "Almoço"}))
    almoco_nonvegan = []
    try:
        almoco_nonvegan.append(get_text_in_li(div_principal)[0])
    except:
        almoco_nonvegan.append("Não há prato principal cadastrado")
    try:
        almoco_nonvegan.append(get_text_in_li(div_acomp)[0])
    except:
        almoco_nonvegan.append("Não há acompanhamento cadastrado")
        
    almoco_vegan = []
    try:
        almoco_vegan.append(get_text_in_li(div_vegan)[0])
    except:
        almoco_vegan.append("Não há almoço vegetariano cadastrado")
    return almoco_nonvegan, almoco_vegan

def get_janta():
    pagina_bs = run_scrapper()
    div_principal = (pagina_bs.find_all("div", {"class": "proteinas"})[0].find("li", {"class": "Janta"}))
    div_acomp = (pagina_bs.find_all("div", {"class": "acompanhamentos"})[0].find("li", {"class": "Janta"}))
    div_vegan = (pagina_bs.find_all("div", {"class": "vegetariano"})[0].find("li", {"class": "Janta"}))
    janta_nonvegan = []
    try:
        janta_nonvegan.append(get_text_in_li(div_principal)[0])
    except:
        janta_nonvegan.append("Não há jantar cadastrado")
    try:
        janta_nonvegan.append(get_text_in_li(div_acomp)[0])
    except:
        janta_nonvegan.append("Não há acompanhamento do jantar cadastrado")
        
    janta_vegan = []
    try:
        janta_vegan.append(get_text_in_li(div_vegan)[0])
    except:
        janta_vegan.append("Não há jantar vegetariano cadastrado")
    return janta_nonvegan, janta_vegan

def get_cardapio():
    pagina_bs = run_scrapper()
    div_principal = (pagina_bs.find_all("div", {"class": "proteinas"})[0].find("li", {"class": "Almoço"}))
    div_acomp = (pagina_bs.find_all("div", {"class": "acompanhamentos"})[0].find("li", {"class": "Almoço"}))
    div_vegan = (pagina_bs.find_all("div", {"class": "vegetariano"})[0].find("li", {"class": "Almoço"}))
    almoco_nonvegan = []
    try:
        almoco_nonvegan.append(get_text_in_li(div_principal)[0])
    except:
        almoco_nonvegan.append("Não há prato principal cadastrado")
    try:
        almoco_nonvegan.append(get_text_in_li(div_acomp)[0])
    except:
        almoco_nonvegan.append("Não há acompanhamento cadastrado")
        
    almoco_vegan = []
    try:
        almoco_vegan.append(get_text_in_li(div_vegan)[0])
    except:
        almoco_vegan.append("Não há almoço vegetariano cadastrado")
    
    
    div_principal = (pagina_bs.find_all("div", {"class": "proteinas"})[0].find("li", {"class": "Janta"}))
    div_acomp = (pagina_bs.find_all("div", {"class": "acompanhamentos"})[0].find("li", {"class": "Janta"}))
    div_vegan = (pagina_bs.find_all("div", {"class": "vegetariano"})[0].find("li", {"class": "Janta"}))
    janta_nonvegan = []
    try:
        janta_nonvegan.append(get_text_in_li(div_principal)[0])
    except:
        janta_nonvegan.append("Não há jantar cadastrado")
    try:
        janta_nonvegan.append(get_text_in_li(div_acomp)[0])
    except:
        janta_nonvegan.append("Não há acompanhamento do jantar cadastrado")
        
    janta_vegan = []
    try:
        janta_vegan.append(get_text_in_li(div_vegan)[0])
    except:
        janta_vegan.append("Não há jantar vegetariano cadastrado")
    return almoco_nonvegan, almoco_vegan, janta_nonvegan, janta_vegan

def get_cardapio_string():
    cardapio = get_cardapio()
    string_card = ("Almoço\nProteínas:\n"+ cardapio[0][0]+"\nAcompanhamentos:\n"+cardapio[0][1]+"\n"+("-"*30)+
                   "\nVegetariano:\n"+cardapio[1][0]+ "\n"+("-"*30)+ "\n"+"Jantar\nProteínas:\n"+cardapio[2][0]+
                   "\nAcompanhamentos:\n"+cardapio[2][1]+"\n"+("-"*30)+"\nVegetariano:\n"+cardapio[3][0])
    return string_card