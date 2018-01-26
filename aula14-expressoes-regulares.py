import re
import requests

req = requests.get('http://www.pernambucanas.com.br/fale-conosco')
strteste = '0x00s4d@0x00s4d.com'

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\,-]+', req.text)
padrao2 = re.findall(r'[\w\.-]+@[\w-]+\.[\w\,-]+', strteste)
if padrao:
    print(padrao)
else:
    print('Padrao nao encontrado')
if padrao2:
    print(padrao2)
else:
    print('Padrao nao encontrado')

