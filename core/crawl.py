#!/usr/bin/env python
#-*- coding:utf-8 -*-


# TODO
# corigir o bug de 'getFrom', 
# 
"""
	bug descriasao:
	  parece que ando os valores da docinario sao 'int' e retorna do a pagina do dia de hoje
	  - corigir: eu acho que os valores devem ser 'str', mais eu devo fazer uma conversercao para o 'mktime'
"""

import sys
import os
import requests
from parse import Parser
import time
import datetime

sys.path.insert(1, os.path.join('..'))
from training import basic


# url sabesp form : http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx
class Crawl():
    
    def __init__(self, url):
        self.url = url
        self.parserObj = Parser()
    
    def getWebPage(self, form=dict()):
        """
            form -> dicionario data requerido do formulario web
            --
            retorna uma string representado o html da 'url' com a requesicao do formulario preechida
        """
        htmlPage = requests.get(self.url, data=form)# requesicao do formaluario com o metodo 'post'
        assert htmlPage.status_code == 200, "Falha ao fazer a requesicao"
        return htmlPage.content
    
    def getTimestamp(self, dataDict):
        """
            retorna o 'timestamp' do dicionario 'dataDict'
        """
        return time.mktime(
                datetime.date(*dataDict.values()).timetuple()
            )# convert '{'cmbAno': 2015,'cmbMes': 1,'cmbDia': 18}' em timestamp
            
    def getForm(self, dictDate):
        """
            'dictDate' -> dicionario de representa a date da requesicao
            --
            retorna um dicionario com: {json:{'sistema': nivel, ...}, date: timestamp}
        """
        # 'dictDate' == {'cmbAno': '2015','cmbMes': '1','cmbDia': '18'}# ano, mes, dia
        json = self.parserObj.convert(self.getWebPage(dictDate))
        return {'json': json, 'date': self.getTimestamp(dictDate)}
        
    
    
        
        
