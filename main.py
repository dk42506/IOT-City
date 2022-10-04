from flask import Flask, render_template, request

f = open('templates/index.html', 'w')

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return user
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()

