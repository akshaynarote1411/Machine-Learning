pip install Flask

from flask import Flask  

app= Flask(__name__)

@app.route("/")
def home():
    return('Welcome')

@app.route("/greet1")
def greet1():
    return('Good morning')

@app.route("/greet2")
def greet2():
    return('good eve')

@app.route("/greet3/go")
def greet3():
    return('good night')

if __name__=="__main__":
    app.run(debug=True)