from flask import Flask, render_template, request
from data import Students
app=Flask(__name__)

getstudents = Students()

@app.route('/students')
def stud():
    return render_template('studentlist.html',mystudentlist=getstudents)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')   

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')       
      
@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getname=request.form['name']
        return render_template('result.html',newname=getname) 

if(__name__=='__main__'):
    app.run(debug=True)