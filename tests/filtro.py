#!/usr/bin/env python
#-*- coding:utf-8 -*-

import basic

if __name__ == "__main__":
	#basic.main('//empregado[@cod="E01"]')# retorna todos os nodes 'empregado' que tenha 'cod="E01"' como key/value
	#basic.main('//empregado[nome="Ana"]') # todos os nodes 'empregado' que tenha um child node 'nome' com valor 'Ana'
	#basic.main('/empregados/empregado[1]')# retoran o primeiro node 'empregado', filhos de 'empregados'
	#basic.main('//empregado[@cod="E01" and @dept="D01"]/sobrenome')# retorna o node 'sobrenome' do empregado que tenha 'cod="E01" dept="D01"'
	basic.main('//empregado[inicial-meio]')# node 'empregado' que tenha um filho node 'inicial-meio'
	
	
	
