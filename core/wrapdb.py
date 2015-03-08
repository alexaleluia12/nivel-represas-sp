#!/usr/bin/env python
#-*- coding:utf-8 -*-

import shelve
import os
from contextlib import closing
import re

def sanity(val, vtype, interval=None):
    if type(str) != type(vtype):#
        raise TypeError("{0} invalid type 'try: int or str'"\
                       .format(repr(vtype)))
    valBool = type(val) == vtype
    if interval == None:
        return valBool
    assert type(val) == type(interval[0]) == type(interval[1]), "the \
                                    interval need to be the same type"

    intervalBool = val >= interval[0] and val <= interval[1]
    return valBool and intervalBool

def check(func):
    valueKeys = [
        'Guarapiranga', 
        'Rio Claro',
        'Cantareira',
        'Rio Grande', 
        'Cotia',
        'Alto Tiete'
    ]
    valueKeys = set(valueKeys)
    def decored(*args, **kargs):
        data = args[-1]
        match = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', data['date'])
        if match:
            groups = match.groups()
            month = sanity(int(groups[1]), int, (1, 12))
            day = sanity(int(groups[2]), int, (1, 31))
            originKeys = set(data['json'].keys())
            keysEqual = valueKeys == originKeys
            if month and day:
                if keysEqual:
                    values = data['json'].values()
                    for i in values:
                        floatMatch = re.search(r'\d+\.\d+', i)
                        if not floatMatch:
                            raise TypeError("The value shold be a string \
                                             that can be convert to float")
                    return func(*args, **kargs)
                else:
                    raise TypeError("Invalid keys for json -> {0}".\
                                    format(originKeys))
            else:
                raise TypeError("Invalid month or day")
        else:
            raise TypeError("Invalid date format -> {0}".format(data['date']))
    return decored

DBFILE = os.path.join('..', 'db', 'sb.db')

class Db(object):
    @check
    def save(self, data, replace=False):
        """
        D.save(data, replace=False) -> retonorna None, salva a data no banco.

        data dever estar no 
        formato: {'date': 'xxxx-xx-xx', 'json': {'Guarapiranga': '38.1',...}
        replace=True -> para que um elemento que já exista no banco seja
         alterado.
        """
        alreadThere = self.getOne(data['date'])
        def innerSave():
            with closing(shelve.open(DBFILE)) as f:
                k = data['date']
                f[k] = data
        if not replace and not alreadThere:
            innerSave()
        elif alreadThere and replace:
            innerSave()
        else:
            raise RunTimeError("It seems thar You are wear the wrong \
                               combinatio o arguments")

    def getOne(self, strDate):
        """
        D.getOne(strDate) -> retorna: 
            {'date': '20xx-xx-xx', 'json': {'Guarapiranga': '38.1',...}}
            se a strDate estiver salva, caso contrario None
            
            strDate deve ser uma string parecido com '2010-03-12' 
            ('ano-mes-dia'), caso o mes tenha um digito 
            ele deve ser precedido de zero 
        """

        with closing(shelve.open(DBFILE)) as f:
            return f.get(strDate, None)

    def excludeOne(self, strDate):
        """
        D.excludeOne(strDate) -> exclui a data referente a key strDate, 
            retorna True caso o elemento foi excluido com sucesso ou False
            caso strDate nao esteja no db.
            
            strDate deve ser uma string parecido com '2010-03-12' 
            ('ano-mes-dia'), caso o mes tenha um digito 
            ele deve ser precedido de zero
        """
        with closing(shelve.open(DBFILE)) as f:
            try:
                del f[strDate]
                return True
            except KeyError, err:
                False

    def getAll(self):
        """
            retorna um generator onde cada elemento e um dicionario 
            parecido com 
            {'date': '20xx-xx-xx', 'json': {'Guarapiranga': '38.1',...}}
        """
        
        with closing(shelve.open(DBFILE)) as f:
            for el in f:
                yield f[el]

    def length(self):
        """
            retorna o a quantidade de registro no banco de dados
        """
        return len(list(self.getAll()))
