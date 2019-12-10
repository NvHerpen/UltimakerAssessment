import string
import random
from datetime import date
from flask import Flask, request, escape, json, jsonify
app = Flask(__name__)

@app.route("/", methods=["POST"])
def curlPost():
    if request.method == "POST":
        data = request.get_json(force=True)

        # Open file for reading
        with open('json.json', 'r') as f:
            dict = json.load(f)

        for entry in dict:

            # Check for duplicate
            if entry['full_url'] == data['full_url']:
                # Throw error
                return "Found in json, terminating"

        # Shorten & add fields to dictionary
        data['short_url'] = shortenUrl(data['full_url'])
        data['created'] = date.today()
        data['nShortened'] = 1

        # Merge data to dict
        dict.append(data)
        print(dict)

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
# Write new entry to json

# Make function (2) that converts full url to small url by randomising                  V
# Extend by checking existence in json & echo outcome

# Extend function 1 to append entry to json
# Extend by saving json

# Make function that accepts short url (short when length<10)