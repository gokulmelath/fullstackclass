from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'welcome to flask'
@app.route('/home')
def home():
    return 'welcome to Home'
@app.route('/about')
def about():
    return 'welcome to aboutpage'        

if(__name__=='__main__'):
    app.run(debug=True)