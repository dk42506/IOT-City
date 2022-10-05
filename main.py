from pexpect import pxssh
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def homePost():
    text = request.form['nm']
    processed_text = text.upper()
    ssh = pxssh.pxssh()
    #("host", "user", "password")
    ssh.login("10.4.2.5", "icsserver", "password")
    # get rid of this command and add ("python3 lcdscreen.py " + str(processed_text)
    ssh.sendline("python3 lcdscreen.py " + str(processed_text))
    return render_template("index.html", variable=processed_text)

if __name__ == "__main__":
    app.run()