from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'counter123456789'




@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template("index.html")




@app.route('/2', methods=['POST'])
def count2():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')


app.run(debug=True)
