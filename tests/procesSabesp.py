#!/usr/bin/env python
#-*- coding:utf-8 -*-



"""
importane:

data em que os dado foram pegos: 31, dez, 2014

site: http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx
"""

from lxml import etree
from lxml.html.soupparser import fromstring
import basic
from pprint import pprint
import string
import re

# string : S , list : L

def helperSplit(obj):
    """
        short-cut para st[re.search(x,st).start():] 
        obj eh Math object
    """
    return obj.string[obj.start():]

def strNumConvert(elemento):	
    """ pega string no formato '  9,5 %  ' e convert para '9.5'  """
    elemento = elemento.translate(string.maketrans('%,', ' .'))
    return elemento.strip()
    
def strIBNConvert(elemento):
    """ pega string no formato 'imagens/sistemaCantareira.gif' e convert para Cantareira """
    elemento.strip()   
    newElemento = re.sub(r'i[\w].+/', '', elemento)# newElemento ==  'sistemaCantareira.gif'
    newElemento = re.sub(r'\.[\w].+', '', newElemento)# newElemento == 'sistemaCantareira'
    newElemento = helperSplit(re.search(r'[A-Z]', newElemento))# newElemento == 'Cantareira'
    return newElemento
    

def main():
    htmlContent = fromstring(basic.getContent('sabespe'))# forma de caregar 'html' que possivelmente nao segue padra XML
    localLS = htmlContent.xpath('//table[@id="tabDados"]/tr//@src')	
    quantidadeLS = htmlContent.xpath('//table[@id="tabDados"]/tr//td[contains(., "%")]/text()')
    # localLS[0] == 'imagens/sistemaCantareira.gif'
    # quantidadeLS[0] == ''7,2 %''
    nivel = map(strNumConvert, quantidadeLS)
    #pprint(nivel)
    

if __name__ == "__main__":
    print(strIBNConvert('imagens/sistemaCantareira.gif'))
     



