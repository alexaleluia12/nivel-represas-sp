#-*- coding:utf-8 -*-
from __future__ import print_function

import re

regex = re.compile(r'[A-Z]')

def splitUpper(tarString):
    listElements = []
    scanner = regex.finditer(tarString)
    end = 0
    start = 0
    
    for match in scanner:
        if match.start() == 0:# pula o primeiro
            continue
        end = match.start()
        listElements.append(tarString[start:end])
        start = end
        # ainda resta mais uma string p/ adicionar depois do for
    listElements.append(tarString[start:])
    
    return listElements



def ndivide(st):
    new_st = st[1:]
    scanner = regex.finditer(new_st)
    
    match = next(scanner)
    local_start = match.start() + 1
    local_end = 0
    yield st[:local_start]
    
    local_start -= 1
    for i in scanner:
        local_end = i.start()
        yield new_st[local_start: local_end]
        local_start = local_end
    
    yield new_st[local_start:]




# SaoCarlosDaBara

## mediar performace
def test_ndivide(st):
    print(' '.join(ndivide(st)))

def test_splitUpper(st):
    print(' '.join(splitUpper(st)))

# resultado
"""
test_ndivide

Sao Carlos Da Bara E Uma Cidade Muito Bonita Para Se Ver

real	0m0.019s
user	0m0.015s
sys	0m0.004s




###
test_splitUpper

Sao Carlos Da Bara E Uma Cidade Muito Bonita Para Se Ver

real	0m0.020s
user	0m0.016s
sys	0m0.004s


"""


if __name__ == "__main__":
    str_test = "SaoCarlosDaBaraEUmaCidadeMuitoBonitaParaSeVer"
    test_ndivide(str_test)
