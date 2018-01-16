from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST", "GET"])
def process():
    print request.form['name']
    return redirect('/')


app.run(debug=True)
