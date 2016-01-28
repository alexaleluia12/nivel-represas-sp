#-*- coding:utf-8 -*-


import datetime


import dryscrape

from parse import Parser
from names import names



dryscrape.start_xvfb()

# url sabesp form : http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx
class Crawl(object):
    
    def __init__(self, url):
        self.url = url
        self.parserObj = Parser()
        self.browser = dryscrape.Session(base_url=self.url)
    
    def getWebPage(self, form):
        """
        form -> dicionario data requerido do formulario web
        --
        retorna uma string representado o html da 'url' com a requesicao do
         formulario preechida
        """
        
        dia = names.day
        mes = names.month
        ano = names.year
        self.browser.visit(self.url)
        
        ## preenche o formulario
        
        _dia = self.browser.at_css('#' + dia)
        _dia.set(form[dia])
        
        _mes = self.browser.at_css('#' + mes)
        _mes.set(form[mes])
        
        _ano = self.browser.at_css('#' + ano)
        _ano.set(form[ano])
        
        ## submit
        botao = self.browser.at_xpath('//*[@id="Imagebutton1"]')
        assert botao
        botao.click()
        return self.browser.document()
        
    
    def getDateStr(self, dataDict):
        """
        retorna uma str 'ano-mes-dia' do dicionario dataDict
        """
        formatStr = '%Y-%m-%d'
        return datetime.datetime(*dataDict.values()).strftime(formatStr)
            
            
    def getForm(self, dictDate):
        """
        'dictDate' -> dicionario de representa a date da requesicao
        --
        retorna um dicionario com: 
            {json:{'sistema': 'nivel', ...}, date: timestamp}
        """
        # 'dictDate' == {'cmbAno': 2015,'cmbMes': 1,'cmbDia': 18}# ano, mes, dia
        json = self.parserObj.convert(self.getWebPage(dictDate))
        return {'json': json, 'date': self.getDateStr(dictDate)}

