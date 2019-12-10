import string
from random import random
from datetime import date
from flask import Flask, request, escape, json, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST"])
def postFullUrl():
    if request.method == "POST":
        data = request.get_json(force=True)

        # Without https://www. in front of the domain, redirect doesn't work.
        if 'https://www.' not in data['full_url']:
            data['full_url'] = 'https://www.' + data['full_url']

        # Open file for reading
        # If not exists, create one.
        with open('json.json', 'r') as f:
            dict = json.load(f)

        for entry in dict:
            # Check for duplicate
            if entry['full_url'] == data['full_url']:
                entry['nUsed'] += 1
                updateJSON(dict)

                # Return existing short_url
                return jsonify(short_url=entry['short_url'])

        # Full_url is unique --> shorten & add to json
        data['short_url'] = shortenUrl(data['full_url'])
        data['created'] = date.today()
        data['nUsed'] = 1

        # Merge data to dict & overwrite json
        dict.append(data)
        updateJSON(dict)

        # Return new short_url
        return jsonify(short_url=data['short_url'])

@app.route('/ultm.kr/<path:short_url>', methods=["GET"])
def getFullUrl(short_url):
    # Open file for reading
    # If not exists, create one.
    with open('json.json', 'r') as f:
        dict = json.load(f)

    for entry in dict:
        if entry['short_url'] == "ultm.kr/" + short_url:
            entry['nUsed'] += 1
            updateJSON(dict)
            return redirect(entry['full_url'], code=302)

    return "This short URL is unknown"

@app.route('/ultm.kr/<path:short_url>/stats', methods=["GET"])
def getStats(short_url):
    with open('json.json', 'r') as f:
        dict = json.load(f)

    for entry in dict:
        if entry['short_url'] == "ultm.kr/" + short_url:
            return jsonify(full_url = entry["full_url"],
                           short_url = entry["short_url"],
                           created = entry['created'],
                           nUsed = entry['nUsed'])


    return "This short URL is unknown"

def shortenUrl(full_url):
    # Shorten url appendix to 6 characters
    short_url = 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Read json file & check for duplicates
    with open('json.json', 'r') as f:
        dict = json.load(f)
    while(any([entry['short_url']==short_url for entry in dict])):
        short_url = 'ultm.kr/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    return short_url

def updateJSON(dict):
    with open('json.json', 'w') as f:
        json.dump(dict, f, indent=4, sort_keys=True)
    return

if __name__ == "__main__":
    app.run()