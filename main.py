import paramiko
import sys
from flask import Flask, render_template, request

def billboard(processed_text):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('10.4.2.41', username= 'icsserver', password= 'password')
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('python lcdScreen ' + str(processed_text))
    sys.exit()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def homePost():
    text = request.form['nm']
    processed_text = text.upper()
    billboard(processed_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

