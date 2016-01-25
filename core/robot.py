#-*- coding:utf-8 -*-
from __future__ import print_function

from datetime import datetime, timedelta
import copy
import pprint


from crawl import Crawl
from wrapdb import Db
from names import names

# dados da sabesp estao disponiveis desde 2003

# TODO
"""
get_between
  o nome do arquivo criado vai ser a (start+end)
  vai pegar os dados apartir de start ate end inclisivo

criar uma property get no DBFILE em wrapdb.py

pegar mudar o parser pq o dados mais atuais da pagina foram alterados

fazer validacoes no get_between

limpar as dependencias que eu nao uso
"""

mainData = {names.year: None, names.month: None, names.day: None}
URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"
date_str = '%Y-%m-%d'

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
    
    
    def get_between(self, start, end):
        """
        start and end should be datetime.datetime instance
        
        start+ (2003, 1, 1)
        end less or equal then today
        """
        
        assert isinstance(start, datetime)
        assert isinstance(end, datetime)
        assert start < end
        
        strftime = datetime.strftime
        self.db.set_DBFILE(
            strftime(start, date_str) + "+" + strftime(end, date_str)
        )
        
        
        # write all the data in the file at once
        lst_dict = self._helper_get_between(start, end)
        self.db.save_iter(lst_dict)
    
    def _helper_get_between(self, start, end):
        day = timedelta(days=1)
        
        yield self.work(start)
        while start <= end:
            start = start + day
            yield self.work(start)
        
    
    def work(self, time):
        assert isinstance(time, datetime)
        dayCat = fillDict(mainData, time)
        data = self.crawler.getForm(dayCat)
        return data

if __name__ == '__main__':
#    d = [2010, 4, 25]
#    Slave().work(*d)
    s = Slave()
    a = datetime(2010, 4, 1)
    b = datetime(2010, 4, 9)
    
    s.get_between(a, b)
  
