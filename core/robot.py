#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime
import copy
import pprint

from crawl import Crawl
from wrapdb import Db

# TODO
# passar dados por linha de comando

mainData = {'cmbAno': None,'cmbMes': None,'cmbDia': None}
URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"

def fillDict(valDict, nowDate=datetime.now()):
    """
    retorna dicionario com os valeres preenchidos com a respectiva data de hoje
    """
    cMes = "cmbMes"
    cAno = "cmbAno"
    cDia = "cmbDia"
    copyDict = copy.deepcopy(valDict)
    copyDict[cAno] = nowDate.year
    copyDict[cMes] = nowDate.month
    copyDict[cDia] = nowDate.day
    return copyDict
    


class Slave(object):

    def __init__(self):
        self.crawler = Crawl(URL)
        self.db = Db() 
        
    def work(self, *args):
        dayCat = fillDict(mainData, datetime(*args))
        data = self.crawler.getForm(dayCat)
        self.db.save(data)
        print('OK')
        pprint.pprint(data)
    

if __name__ == '__main__':
    d = [2013, 3, 20]
    Slave().work(*d)
  
