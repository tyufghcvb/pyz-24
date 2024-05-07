from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello_world():
    return "<p>Hello, World!</p>"
gi

if __name__ == '__main__':
    app.run(debug=True)