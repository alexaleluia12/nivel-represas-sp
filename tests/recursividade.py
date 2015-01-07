#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re

# TODO
def splitNotDelete(stRegular, tarString):
    """ stRegular: string que representa uma regularExp
        tarString: string que sera esplitada
        
        --
        retorna um lista de string, mas nao esclui os caraceter da Match,
        e descondidera a primeria letra da string
    """
    listElements = []
    allUpper = re.findall(stRegular, tarString)
    assert(allUpper)
    print(allUpper)
    last = allUpper[-1]
    firstChar = tarString[0]
    for letra in allUpper:  
        if firstChar == letra:
            continue     
        indice = tarString.find(letra)     
        listElements.append(tarString[:indice])
        tarString = tarString[indice:]# a ultima sai aqui, entao adiciona depois do for        
    listElements.append(tarString)
    return listElements
    
        
    

def inserirSpaco(st):
    def spaco(stInner, indice):
        assert(indice >= 0)
        return stInner[:indice] + " " + stInner[indice:]
        
    allUpper = re.findall(r'[A-Z]', st)
    print(allUpper)
    if not allUpper:
        return st
    for letra in allUpper:
        print(st)
        st = spaco(st, st.find(letra))
    return st
    
    
        
    
# SaoCarlosDaBara

if __name__ == "__main__":
    print(splitNotDelete(r'[A-Z]',"SaoCarlosDaBara"))    
    print(splitNotDelete(r'[A-Z]',"saoCarlosDaBara"))
    
