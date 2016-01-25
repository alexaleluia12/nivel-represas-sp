#-*- coding:utf-8 -*-

import os
from contextlib import closing
import json

import decorators


class Db(object):
    def __init__(self):
        self._DBFILE = ""

    
    def save_iter(self, iterable):
        with open(self._DBFILE, 'wt') as f:
            str_json_lst = (json.dumps(data) + '\n' for data in iterable)
            f.writelines(str_json_lst)
    
    def set_DBFILE(self, name):
        self._DBFILE = os.path.join('..', 'db', (name + '.json'))

