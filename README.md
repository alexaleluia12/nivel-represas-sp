nivel-represas-sp
=================

aplicação que pega os Dados importantes da Sabesp

[font: Sabesp](http://www2.sabesp.com.br/mananciais/DivulgacaoSiteSabesp.aspx)

> nota:
Foi usado a biblioteca 'requests' nesse projeto.
Porem eu não consegui fazer requições de dias anteriores ao dia atual.
Eu seria muito grato se alguem coseguise fazer isso.

Local onde é feito a requesição:
'crawl.py' -> Crawl -> getWebPage

---
> dependências:

python 2.7
```sh
$ pip install -r requerimentos.txt

```

talvez você tenha algum problema em instalar o lxml
veja http://lxml.de/installation.html
