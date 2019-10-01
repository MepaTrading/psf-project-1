import requests
from bs4 import BeautifulSoup

def find_tag(father_tag):
    code_tag = []
    for tag in father_tag:
        span_tag = tag.find('span')
        for tag_2 in span_tag:
            code_tag.append(str(tag_2) + '.SA')

    return code_tag

def get_codes(carteiras):
    code_list = []
    for carteira in carteiras:
        page = requests.get(carteira)
        soup = BeautifulSoup(page.text, 'html.parser')
        tag_tabela = soup.find_all('td', {"class" : "rgSorted"})
        code_list = find_tag(tag_tabela)
    
    return code_list

carteiras = ['http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IMOB&idioma=pt-br',
            'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=UTIL&idioma=pt-br',
            'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=ICON&idioma=pt-br',
            'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IMAT&idioma=pt-br',
            'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=INDX&idioma=pt-br']
