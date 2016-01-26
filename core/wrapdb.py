#-*- coding:utf-8 -*-
from __future__ import print_function
import os
import json

import decorators


class Db(object):
    def __init__(self):
        self._DBFILE = ""
    
    
    def save_iter(self, iterable):
        assert self.DBFILE != "", "set DBFILE name before save"
        with open(self.DBFILE, 'wt') as f:
            valid_data = (i for i in iterable if decorators.check(i))
            str_json_lst = (json.dumps(data) + '\n' for data in valid_data)
            f.writelines(str_json_lst)
    
    @property
    def DBFILE(self):
        return self._DBFILE
    
    @DBFILE.setter
    def DBFILE(self, value):
        self._DBFILE = os.path.join('..', 'db', (value + '.json'))



