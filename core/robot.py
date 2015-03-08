#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
from datetime import datetime
import copy
import pprint

from crawl import Crawl
from wrapdb import Db

def fillDict(valDict):
    """
        retorna dicionario com os valeres preenchidos com a respectiva data de hoje
    """
    ano = "%Y"
    mes = "%m"
    dia = "%d"
    cMes = "cmbMes"
    cAno = "cmbAno"
    cDia = "cmbDia"
    nowDate = datetime.now()
    copy = copy.deepcopy(valDict)
    copy[cAno] = int(nowDate.strftime(ano))
    copy[cMes] = int(nowDate.strftime(mes))
    copy[cDia] = int(nowDate.strftime(dia))
    return copy
    

class Slave(object):

    URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"
    mainData = {'cmbAno': None,'cmbMes': None,'cmbDia': None}
    def __init__(self):
        self.crawler = Crawl(self.URL)
        self.db      = Db() 
        
    def work(self):
        dayCat = fillDict(self.mainData)
        data = self.crawler.getForm(dayCat)
        self.db.save(data)
        print('OK')
        pprint.pprint(data)

if __name__ == '__main__':
    Slave().work()
  
