#!/usr/bin/env python
#-*- coding:utf-8 -*-

# TODO

# pegar essa extrutura de dados acima todos os dias no site da Sabespe (nao sei exata mento como vou fazer isso)

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

def splitUpper(tarString):
    """ 
        tarString: string que sera esplitada
        
        --
        retorna um lista de string, mas nao esclui os caraceter da Match,
        e descondidera a primeria letra da string, usa letra maiusculas como referencia
    """
    listElements = []
    stRegular = r'[A-Z]'
    allUpper = re.findall(stRegular, tarString)    
    assert allUpper, "A string '" + tarString  + "' deve tem mais de uma letra maiuscula"
    last = allUpper[-1]
    firstChar = tarString[0]
    for letra in allUpper:  
        if firstChar == letra:
            continue     
        indice = tarString.find(letra)     
        listElements.append(tarString[:indice])
        tarString = tarString[indice:]# a ultima string sai aqui, entao adiciona depois do for        
    listElements.append(tarString)
    return listElements
    

def stripFirst(obj):
    """ obj: Math object
    
        --            
        retorna uma string mais human legivel,
        tira a paravra 'sistema' e insere espacos em branco onde eh conveniente 
        
    """
    stStripada = obj.string[obj.start():]
    return ' '.join(splitUpper(stStripada))

def strNumConvert(elemento):	
    """ pega string no formato '  9,5 %  ' e convert para '9.5'  """
    elemento = elemento.translate(string.maketrans('%,', ' .'))
    return elemento.strip()
    
def strIBNConvert(elemento):
    """ pega string no formato 'imagens/sistemaCantareira.gif' e convert para Cantareira """
    elemento.strip()   
    newElemento = re.sub(r'i[\w].+/', '', elemento)# newElemento ==  'sistemaCantareira.gif', tira 'imagens'
    newElemento = re.sub(r'\.[\w].+', '', newElemento)# newElemento == 'sistemaCantareira'  , tira '.gif'
    newElemento = stripFirst(re.search(r'[A-Z]', newElemento))# newElemento == 'Cantareira', tira 'sistema'
    return newElemento
    

def main():
    htmlContent = fromstring(basic.getContent('sabespe'))# forma de caregar 'html' que possivelmente nao segue padrao XML
    localLS = htmlContent.xpath('//table[@id="tabDados"]/tr//@src')	
    quantidadeLS = htmlContent.xpath('//table[@id="tabDados"]/tr//td[contains(., "%")]/text()')
    # localLS[0] == 'imagens/sistemaCantareira.gif'
    # quantidadeLS[0] == ''7,2 %''
    niveis = map(strNumConvert, quantidadeLS)
    represas = map(strIBNConvert, localLS)
    dictData = dict(zip(represas, niveis)) # {"Sistema", nivel, ...}
    pprint(dictData)
    

if __name__ == "__main__":    
    main()
     



