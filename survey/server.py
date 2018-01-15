from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def showsurvey():
    return render_template('index.html')

@app.route ('/processdata', methods = ['Post'])
def process():
    print request.form ["name"]
    print request.form  ["language"]
    print request.form  ["location"]
    return render_template('result.html', personName =name)

app.run(debug=True)
