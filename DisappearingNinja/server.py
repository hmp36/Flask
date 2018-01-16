from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninja')
def ninja():
    return render_template("ninja.html")


@app.route('/ninja/<color>')
def ninjas(color):
    color = color.lower()
    if color == 'blue' or color == 'red' or color == 'purple' or color == 'orange':
        return render_template("many.html", color=color)
    else:
        return render_template('none.html', color="notapril")


app.run(debug=True)
