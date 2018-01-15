from flask import Flask, render_template, redirect, session, request
import random 
app=Flask(__name__)
app.secret_key = "Golden Key"

@app.route ('/')
def home():
      if 'yourGold' not in session:
          session ['yourGold'] = 0
      if  'activity' not in session:
          session ['activity'] = []    
      return render_template('index.html')

@app.route ('/process_money', methods = ['POST'])
def processGold():
    
    
    if request.form['location'] =='farm':
       print request.form ['location']
       goldEarned = random.randint(10,20)
       session ['yourGold'] = session ['yourGold'] + goldEarned
       newstr = 'Earned {} gold from the {}!'.format(goldEarned,request.form['location'])
       session ['activity'].append(newstr)
       

    elif request.form['location'] =='cave':
        print request.form ['location']
        goldEarned = random.randint(5,10)
        session ['yourGold'] = session ['yourGold'] + goldEarned
        newstr = 'Earned {} gold from the {}!'.format(goldEarned,request.form['location'])
        session ['activity'].append(newstr)

    elif request.form['location'] =='house':
        print request.form ['location']
        goldEarned = random.randint(2,5)
        session ['yourGold'] = session ['yourGold'] + goldEarned
        newstr = 'Earned {} gold from the {}!'.format(goldEarned,request.form['location'])
        session ['activity'].append(newstr)

    elif request.form['location'] =='casino':
        print request.form ['location']
        goldEarned = random.randint(-50,50)
        session ['yourGold'] = session ['yourGold'] + goldEarned
        if goldEarned >= 0:
            newstr = 'Earned {} gold from the {}!'.format(goldEarned,request.form['location'])
        else:
            newstr = 'Lost {} gold from the {}!'.format(goldEarned,request.form['location'])  
        session ['activity'].append(newstr)     
          







       

    return redirect('/')

app.run(debug = True)