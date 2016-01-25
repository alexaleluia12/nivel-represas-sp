#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime
import copy
import pprint

from crawl import Crawl
from wrapdb import Db
from names import names

# TODO
# usar json ao inves de pickel
# passar dados por linha de comando criar outro modulo py

mainData = {names.year: None, names.month: None, names.day: None}
URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"

def fillDict(valDict, nowDate=datetime.now()):
    """
    retorna dicionario com os valeres preenchidos com a respectiva data de hoje
    """
    copyDict = copy.deepcopy(valDict)
    copyDict[names.year] = nowDate.year
    copyDict[names.month] = nowDate.month
    copyDict[names.day] = nowDate.day
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
    d = [2010, 4, 21]
    Slave().work(*d)
  
