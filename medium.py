import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cnn():
    url = 'https://search.api.cnn.io/content?q=coronavirus&page=6'
    json_data = requests.get(url).json()
    data = json_data['result']
    return render_template('index.html', data= data)

if __name__ == "__main__":
    app.run(debug=True)