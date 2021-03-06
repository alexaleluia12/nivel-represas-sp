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

fazer isso rodar mais rapido
"""

mainData = {names.year: None, names.month: None, names.day: None}
URL = "http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx"
date_str = '%Y-%m-%d'
start_date = datetime(2003, 1, 1)

def fillDict(valDict, nowDate=datetime.now()):
    """
    retorna dicionario com os valeres preenchidos com a respectiva nowDate
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
    
    def get_one(self, date):
        """
        start should be datetime.datetime instance
        start+ (2003, 1, 1)
        end less then today
        save the data on db/start.json
        """
        now = datetime.now()
        now = datetime(now.year, now.month, now.day)
        
        assert isinstance(date, datetime), 'start need to be datetime instance'
        assert date < now, 'date need to be less or equal than yesterday'
        assert date >= start_date, 'no data before \"2003-01-01\"'
        
        strftime = datetime.strftime
        self.db.DBFILE = strftime(date, date_str)
        
        data = self.work(date)
        self.db.save_iter([self.work(date)])
    
    def get_between(self, start, end):
        """
        start and end should be datetime.datetime instance
        start+ (2003, 1, 1)
        end less then today
        save the data on db/start+end.json
        """
        now = datetime.now()
        now = datetime(now.year, now.month, now.day)
        
        assert isinstance(start, datetime), 'start need to be datetime instance'
        assert isinstance(end, datetime), 'end need to be datetime instance'
        assert start < end, 'start need to be less than end'
        assert end < now, 'end need to be less or equal than yesterday'
        assert start >= start_date, 'no data before \"2003-01-01\"'
        
        strftime = datetime.strftime
        self.db.DBFILE = \
            strftime(start, date_str) + "+" + strftime(end, date_str)
        
        
        # write all the data in the file at once
        lst_dict = self._helper_get_between(start, end)
        self.db.save_iter(lst_dict)
    
    def _helper_get_between(self, start, end):
        day = timedelta(days=1)
        
        yield self.work(start)
        while start < end:
            start = start + day
            yield self.work(start)
    
    
    def work(self, time):
        assert isinstance(time, datetime)
        dayCat = fillDict(mainData, time)
        data = self.crawler.getForm(dayCat)
        return data

if __name__ == '__main__':
    s = Slave()
    a = datetime(2016, 1, 19)
    b = datetime(2004, 2, 22)
    
    s.get_one(b)
