#!/usr/bin/env python
#-*- coding:utf-8 -*-

# TODO
# testar tudo isso, deveria ter usado TDD nesse projeto :(

from crawl import Crawl
import threading
from datetime import datetime
from wrapdb import Db

def fillDict(valDict):
    """
        retorna valDict com os valeres preenchidos com a respectiva data de hoje
    """
    ano = "%Y"
    mes = "%m"
    dia = "%d"
    nowDate = datetime.now()
    valDict["cmbAno"] = int(nowDate.strftime(ano))
    valDict["cmbMes"] = int(nowDate.strftime(mes))
    valDict["cmbDia"] = int(nowDate.strftime(dia))
    

class Slave(object):

    URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"
    mainData = {'cmbAno': None,'cmbMes': None,'cmbDia': None}
    def __init__(self):
        self.crawler = Crawl(URL)
        self.db      = Db() 
        
    def work(self):
        dayCat = fillDict(self.mainData)
        data = self.crawler.getForm(dayCat)
        self.db.save(data)
        threading.Timer(86400, self.work).start() # se repete a cada 24h
        

if __name__ == '__main__':
    Slave().work()

        



    
