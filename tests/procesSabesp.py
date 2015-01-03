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

# string : S , list : L

def main():
    htmlContent = fromstring(basic.getContent('sabespe'))
    print('xpath' in dir(htmlContent))
    localLS = htmlContent.xpath('//table[@id="tabDados"]/tr//@src')	
    quantidadeLS = htmlContent.xpath('//table[@id="tabDados"]/tr//td[contains(., "%")]/text()')
    

if __name__ == "__main__":
    main()   
     

"""
o que eu vou usar para tratar os dados retorndado pelo 'lxml'

>>> i = '  9,5 %  '
>>> import string
>>> oi = i.translate(string.maketrans(',%', '. '))
>>> oi
'  9.5    '
>>> io.strip()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'io' is not defined
>>> oi.strip()
'9.5'
>>> float(oi)
9.5

"""

