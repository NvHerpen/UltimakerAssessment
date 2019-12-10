import string
import random
from flask import Flask, request, escape, json, jsonify
app = Flask(__name__)

@app.route('/full_url/<path:full_url>')
def echoPath(full_url):
    short_url = randomiseURL(full_url)
    print(full_url + " ::::: " + short_url)
    return 'Short Url = %s' % escape(short_url)

@app.route("/", methods=["POST"])
def curlPost():
    if request.method == "POST":
        full_url = request.get_json(force=True)['full_url']

        # Open file for reading
        with open('json.json', 'r') as f:
            dict = json.load(f)

        for entry in dict:

            # Check for duplicate
            if entry['full_url'] == full_url:
                print('url found in json')
                # Throw error

            # Shorten & add to json
            else:
                short_url = shortenUrl(full_url)
                print(short_url)

    return "Curl"

def shortenUrl(full_url):
    return 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

if __name__ == "__main__":
    app.run()

# Make function (1) that accepts (after localhost:5000/) a url string and echos it      V
# Extend by accepting a JSON POST request and store in local variable                   V
# Open json                                                                             V
# Import json to dict                                                                   V
# Search dict for POST url                                                              V

# Make function (2) that converts full url to small url by randomising                  V
# Extend by checking existence in json & echo outcome

# Extend function 1 to append entry to json
# Extend by saving json

# Make function that accepts short url (short when length<10)