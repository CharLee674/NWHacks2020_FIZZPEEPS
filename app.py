from flask import Flask, render_template, request, url_for
from test import getSentiment
import base64
from io import BytesIO

from matplotlib.figure import Figure

#Creates an instance of the Flask app under the name 'app'
app = Flask(__name__)
app.debug = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#Sets up the route to url / with function home
@app.route('/', methods = ['GET', 'POST']) #REST api method usage
def home():
    if request.method == 'POST': #If the user asks for the results
        #Taken from https://matplotlib.org/faq/howto_faq.html#how-to-use-matplotlib-in-a-web-application-server 
        """# Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot([1, 2])
        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return f"<img src='data:image/png;base64,{data}'/>"""
        #This receives the request from the entry in the page
        entry = request.form.get("entry")
        #This uses the getSentiment function in test.py in our folder
        sentiment = getSentiment(entry)
        return render_template("index.html", sentiment=sentiment) #this renders the html file inside the templates folder
    if request.method == 'GET': #If the user asks for the webpage
        return render_template("index.html")




@app.route('/getpost')
def getpost():
    return "hi"

#If we wanna make a page with all of our photos and stuff
@app.route('/contributors')
def people():
    return render_template("contributors.html")


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)