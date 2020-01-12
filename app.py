from flask import Flask, render_template, request
from test import getSentiment

app = Flask(__name__)
app.debug = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry = request.form.get("entry")
        sentiment = getSentiment(entry)
        return render_template("index.html", sentiment=sentiment)
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/getpost')
def getpost():
    return "hi"


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)