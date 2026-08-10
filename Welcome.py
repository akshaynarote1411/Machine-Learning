from flask import Flask

app = Flask(__name__)

#@app.route("/")
#def greet():
#   return("Hello World...")

@app.route("/")
def greet1():
    return("Welcome.....")

if __name__ == "__main__":
    app.run()