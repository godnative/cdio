import sys
import mysqlconnect
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/ws')
def ws():
    return render_template('ws.html')


@app.route('/qy')
def qy():
    return render_template('qy.html')


@app.route('/fsfx')
def fsfx():
    return render_template('fsfx.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        cookie = 1
        return render_template('signin-ok.html', username=username)

    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/wsshow', methods=["POST"])
def wsshow():
    return mysqlconnect.wsjson()


@app.route('/qyshow', methods=["POST"])
def qyshow():
    return mysqlconnect.qyjson()


@app.route('/fsshow', methods=["POST"])
def fsshow():
    return mysqlconnect.fsjson()


def quit(signum, frame):
    print("exit")
    sys.exit()


if __name__ == '__main__':
    app.run(debug=True)
