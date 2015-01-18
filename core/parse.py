#!/usr/bin/env python
#-*- coding:utf-8 -*-

from lxml import etree
from lxml.html.soupparser import fromstring
import re
import string

class Parser():

    def __init__(self):
        pass
    
    def _splitUpper(self, tarString):
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
    

    def stripFirst(self, obj):
        """ obj: Math object
        
            --            
            retorna uma string mais human legivel,
            tira a paravra 'sistema' e insere espacos onde eh conveniente 
            
        """
        stStripada = obj.string[obj.start():]
        return ' '.join(self._splitUpper(stStripada))

    def strNumConvert(self, elemento):	
        """ pega string no formato '  9,5 %  ' e convert para '9.5'  """
        elemento = elemento.translate(string.maketrans('%,', ' .'))
        return elemento.strip()
        
    def strIBNConvert(self, elemento):
        """ pega string no formato 'imagens/sistemaCantareira.gif' e convert para Cantareira """
        elemento.strip()   
        newElemento = re.sub(r'i[\w].+/', '', elemento)# newElemento ==  'sistemaCantareira.gif', tira 'imagens'
        newElemento = re.sub(r'\.[\w].+', '', newElemento)# newElemento == 'sistemaCantareira'  , tira '.gif'
        newElemento = self.stripFirst(re.search(r'[A-Z]', newElemento))# newElemento == 'Cantareira', tira 'sistema'
        return newElemento    
    
    def convert(self, xhtml):
        """
            xhtml -> string que representa um codigo html ou xml
            
            retorna dicionario na forma {'SistemaName': volume, ...}
        """
        htmlContent = fromstring(xhtml)
        localLS = htmlContent.xpath('//table[@id="tabDados"]/tr//@src')	
        quantidadeLS = htmlContent.xpath('//table[@id="tabDados"]/tr//td[contains(., "%")]/text()')
        # localLS[0] == 'imagens/sistemaCantareira.gif'
        # quantidadeLS[0] == ''7,2 %''
        niveis = map(self.strNumConvert, quantidadeLS)
        represas = map(self.strIBNConvert, localLS)
        return dict(zip(represas, niveis)) # {"Sistema": nivel, ...}        

    
    
