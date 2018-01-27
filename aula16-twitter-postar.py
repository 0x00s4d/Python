import oauth2
import json
import urllib

consumer_key = '<yourkey>'
consumer_secret = '<yoursecret>'
token_key = 'yourtoken-key'
token_secret = '<yourtoken-secret>'

query = raw_input("Tweetar: ")
query_cod = urllib.quote(query, safe='')
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

req = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_cod, method='POST')
decodificar = req[1].decode()
req_objeto = json.loads(decodificar)
tweets = req_objeto

print(req_objeto)