#!/usr/bin/env python
#-*- coding:utf-8 -*-

import shelve
from contextlib import closing

DBFILE = '../db/sb.db'

class Db(object):
    
    def save(self, data):
        """
        	D.save(data) -> retonorna None, salva a data no banco.
        	
        	data dever estar no formato: {'date': 'xxxx-xx-xx', 'json': {'Guarapiranga': '38.1',...}
        """
        
        with closing(shelve.open(DBFILE)) as f:
            k = data['date']
            f[k] = data

    def getOne(self, strDate):
        """
        	D.save(strDate) -> retorna {'date': '20xx-xx-xx', 'json': {'Guarapiranga': '38.1',...}}
        	    se a strDate estiver salva, caso contrario None
        	    
        	    strDate deve ser uma string parecido com '2010-03-12' ('ano-mes-dia'), caso o mes tenha um digito 
        	    ele deve ser precedido de zero 
        """
        
        with closing(shelve.open(DBFILE)) as f:
            return f.get(strDate, None)      

    def excludeOne(self, strDate):
        """
        	D.excludeOne(strDate) -> exclui a data referente a key strDate, retorna True caso o elemento foi 
        	    excluido com sucesso ou False caso strDate nao esteja no db.
        	    
        	    strDate deve ser uma string parecido com '2010-03-12' ('ano-mes-dia'), caso o mes tenha um digito 
        	    ele deve ser precedido de zero

  
        """
        with closing(shelve.open(DBFILE)) as f:
            try:
                del f[strDate]
                return True
            except KeyError, err:
                False
        

