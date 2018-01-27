import oauth2
import json
import urllib

consumer_key = '<yourkey>'
consumer_secret = '<yoursecret>'
token_key = 'yourtoken-key'
token_secret = '<yourtoken-secret>'

query = raw_input("Pesquisa: ")
query_cod = urllib.quote(query, safe='')
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

req = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_cod + '&lang=pt')
decodificar = req[1].decode()
req_objeto = json.loads(decodificar)
tweets = req_objeto

for tweet in req_objeto['statuses']:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print('')