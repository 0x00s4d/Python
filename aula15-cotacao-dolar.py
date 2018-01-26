import requests
import json
import datetime
import time


while True:
    try:
        URL = 'http://api.promasters.net.br/cotacao/v1/valores'
        response = requests.get(URL)
        cotacao = json.loads(response.text)
    except:
        print('Erro de conexao')

    print('--------------------COTACAO DOLAR '+ str(datetime.datetime.now()) +'--------------------')
    print('Tipo de moeda: ' + cotacao['valores']['USD']['nome'])
    print('Valor: ' + str(cotacao['valores']['USD']['valor']))
    print('Ultima consulta: ' + str(cotacao['valores']['USD']['ultima_consulta']))
    print('Fonte: ' + str(cotacao['valores']['USD']['fonte']))
    print('')
    print('--------------------COTACAO EURO '+ str(datetime.datetime.now()) +'--------------------')
    print('Tipo de moeda: ' + cotacao['valores']['EUR']['nome'])
    print('Valor: ' + str(cotacao['valores']['EUR']['valor']))
    print('Ultima consulta: ' + str(cotacao['valores']['EUR']['ultima_consulta']))
    print('Fonte: ' + str(cotacao['valores']['EUR']['fonte']))
    print('')
    print('--------------------COTACAO BTC '+ str(datetime.datetime.now()) +'--------------------')
    print('Tipo de moeda: ' + cotacao['valores']['BTC']['nome'])
    print('Valor: ' + str(cotacao['valores']['BTC']['valor']))
    print('Ultima consulta: ' + str(cotacao['valores']['BTC']['ultima_consulta']))
    print('Fonte: ' + str(cotacao['valores']['BTC']['fonte']))
    time.sleep(5)