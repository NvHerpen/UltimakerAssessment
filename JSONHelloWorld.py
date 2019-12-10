import string
import random
from flask import Flask, request, escape
app = Flask(__name__)

@app.route('/full_url/<path:full_url>')
def echoPath(full_url):
    short_url = randomiseURL(full_url)
    print(full_url + " ::::: " + short_url)
    return 'Short Url = %s' % escape(short_url)

def randomiseURL(full_url):
    return 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

if __name__ == "__main__":
    app.run()

# Make function (1) that accepts (after localhost:5000/) a url string and echos it      V
# Extend that function by opening a json file
# Extend that by getting json full_url list
# Extend that by searching in list and echo outcome (exists or not)

# Make function (2) that converts full url to small url by randomising                  V
# Extend by checking existence in json & echo outcome

# Extend function 1 to append entry to json
# Extend by saving json

# Make function that accepts short url (short when length<10)