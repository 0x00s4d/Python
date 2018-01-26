import requests
#Beautiful Soup 4 BS4 pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}
cookies= {'Ultima-visita':'10-10-2020'}
dados= {'username':'0x00s4d',
        'password': '0x00s4d123'}
texto=None

try:
    requisicao = requests.post('http://putsreq.com/cx9pSAc70EAyABD3U0a5',
                               headers=cabecalho,
                               cookies=cookies,
                               data=dados)
    texto=requisicao.text

except Exception as error:
    print('Request Error: ', error)

print(texto)

