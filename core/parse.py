#-*- coding:utf-8 -*-

from lxml import etree
from lxml.html.soupparser import fromstring
import re
import string


regex = re.compile(r'[A-Z]')

class Parser(object):
    
    def get_number(self, st):
        match = re.match(r'.+?(\d{2},\d\s%)', st)
        assert match != None
        st = str(match.group(1))
        return st
    
    def _splitUpper(self, tarString):
        """
        Transforma 'HojeFoiDia' em 'Hoje Foi Dia' atraves de um iterator
        """
        listElements = []
        scanner = regex.finditer(tarString)
        end = 0
        start = 0
        
        for match in scanner:
            if match.start() == 0:# pula o primeiro
                continue
            end = match.start()
            listElements.append(tarString[start:end])
            start = end
            # ainda resta mais uma string p/ adicionar depois do for
        listElements.append(tarString[start:])
        
        return listElements
    
    def strNumConvert(self, elemento):	
        """ pega string no formato '  9,5 %  ' e convert para '9.5'  """
        elemento = elemento.translate(string.maketrans('%,', ' .'))
        return elemento.strip()
        
    def strIBNConvert(self, elemento):
        """ 
        pega string no formato 'imagens/sistemaCantareiraDoSul.gif' e convert 
        para 'Cantareira Do Sul'
        """
        elemento.strip()
        m = re.match(r'.+?/sistema([A-Z]\w+).\w+', elemento)
        assert m
        return ' '.join(self._splitUpper(m.group(1)))
    
    def convert(self, xhtml):
        """
        xhtml -> string que representa um codigo html ou xml
        
        retorna dicionario na forma {'SistemaName': 'volume', ...}
        onde 'volume' eh uma string que pode ser vonvertida para
        float
        """
        localLS = xhtml.xpath('//table[@id="tabDados"]//tr//@src')
        # td[contains(., '%')]/text()
        # caso o td corrente '.' tenha '%' pega o texto dele 'text()'
        quantidadeLS = xhtml.xpath(
            '//table[@id="tabDados"]//tr//td[contains(., "%")]/text()'
        )
        # eh necessario um processamento extra devido a mudanca da pagina
        if isinstance(quantidadeLS[0], unicode):
            quantidadeLS = quantidadeLS[2:]
            # pega apenas o tag referente ao sistema cantareira
            cantareira = xhtml.xpath('//table[@id="tabDados"]//tr[2]//td[2]')[0]
            ultimo_filho = cantareira[-1]
            quantidadeLS.insert(0, self.get_number(ultimo_filho.text))
        
        # localLS[0] == 'imagens/sistemaCantareira.gif'
        # quantidadeLS[0] == ''7,2 %''
        niveis = map(self.strNumConvert, quantidadeLS)
        represas = map(self.strIBNConvert, localLS)
        
        # {"Sistema": 'nivel', ...}
        return dict(zip(represas, niveis))
