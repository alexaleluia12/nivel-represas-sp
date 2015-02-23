#!/usr/bin/env python
#-*- coding:utf-8 -*-

# TODO
# 

from crawl import Crawl
import threading
from datetime import datetime
from wrapdb import Db

def fillDict(valDict):
    """
        retorna dicionario com os valeres preenchidos com a respectiva data de hoje
    """
    ano = "%Y"
    mes = "%m"
    dia = "%d"
    nowDate = datetime.now()
    copy = valDict
    copy["cmbAno"] = int(nowDate.strftime(ano))
    copy["cmbMes"] = int(nowDate.strftime(mes))
    copy["cmbDia"] = int(nowDate.strftime(dia))
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
        
        

if __name__ == '__main__':
    Slave().work()
  
