from flask import Flask, render_template, abort


app = Flask(__name__)


@app.route('/')
def show():
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run()