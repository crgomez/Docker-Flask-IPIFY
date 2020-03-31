# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')

def get_identification():
    ip = requests.get('https://api.ipify.org').text

    return 'My public IP address is: {}'.format(ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
