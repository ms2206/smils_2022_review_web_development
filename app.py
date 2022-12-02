from flask import Flask

app = Flask(__name__)


@app.route('/jan/index.html')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
