from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return 'H.O.M.E'

if __name__ == "__main__":
    app.run(debug=True)