import requests

url ='https://search.api.cnn.io/content?q=coronavirus&size=10&page=3'
json_data = requests.get(url).json()

for j in json_data['result']:
    title = j['headline']
    print(title)
