from flask import Flask
app = Flask(__name__)

users = [{"name": "sjaak"},{"name": "koos"}]

@app.route("/user/<user_in>")
def getUser(user_in):
    for user in users:
        if user["name"] == user_in:
            return "{} bestaat gelukkig nog".format(user_in)
    return "{} konden we niet meer vinden".format(user_in)

if __name__ == "__main__":
    app.run()