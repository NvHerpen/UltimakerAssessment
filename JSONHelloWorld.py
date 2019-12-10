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
        # If not exists, create one.
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

        # Merge data to dict & overwrite json
        dict.append(data)
        with open('json.json', 'w') as f:
            json.dump(dict, f, indent=4, sort_keys=True)

    return "Curl"

def shortenUrl(full_url):
    # Shorten url appendix to 6 characters
    short_url = 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Check for duplicates
    with open('json.json', 'r') as f:
        dict = json.load(f)

    while(any([entry['short_url']==short_url for entry in dict])):
        short_url = 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    return short_url

if __name__ == "__main__":
    app.run()

# Make function (1) that accepts (after localhost:5000/) a url string and echos it      V
# Extend by accepting a JSON POST request and store in local variable                   V
# Open json                                                                             V
# Import json to dict                                                                   V
# Search dict for POST url                                                              V
# Write new entry to json                                                               V

# Make function (2) that converts full url to small url by randomising                  V
# Extend by checking existence in json & echo outcome                                   V

# Make function that accepts short url (short when length<10)