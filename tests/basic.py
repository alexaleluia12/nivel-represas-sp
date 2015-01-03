#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	TODO
inserir html com unicode
"""



from lxml import etree

def getContent(localFile):
	with open(localFile) as f:
		return f.read()

def show(obj):	
	try:	
		for element in obj:	
			print(etree.tostring(element, pretty_print=True))
	except TypeError:
		print(obj)
	

def main(strPath, file='xpath.xml'):			
	html = etree.fromstring(getContent(file))
	empregados = html.xpath(strPath)
	show(empregados)

__all__=['main', 'show']
"""

o que retorna e sempre o o ultima node depois de '/'
empregados/empregado → nesse caso todos os empregados

trick atributo:

//@lang 				Selects all attributes that are named lang→str
//title[@lang] 			Selects all the title elements that have an attribute named lang→node
//title[@lang='en'] 	Selects all the title elements that have an attribute named lang with a value of 'en'→node
"""
	

if __name__ == '__main__':
	"""
		>>> print(html.xpath("string()")) # lxml.etree only!
		TEXTTAIL
		>>> print(html.xpath("//text()")) # lxml.etree only!
	"""
	
	#main('/empregados/empregado')# todos os nodes 'empregados'
	#main('/empregados/empregado/nome/text()')# todos as string dos node 'nome' → retorna uma list string
	#main('//@cod')# todos os str valor do atributo 'cod', procura em todos os nodes → retorna list string
	# util para funcaoes: curent node:main('/empregados/.') (equivale) main('/empregados')
	#main('/empregados/empregado/..')# pega pai, 'empregados'
 	#main('//empregado/*') # todos as child 'node' de todos 'empregado' node
	
    

