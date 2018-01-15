from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)
app.secret_key="junior"

@app.route ('/')
def home():
      if 'yourGold' not in session:
          session ['yourGold'] = 0
      return render_template('index.html')

@app.route ('/processGold', methods = ['POST'])
def processGold():
    print request.form
    return redirect('/')    

app.run(debug = True)