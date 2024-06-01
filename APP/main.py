from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('userregister.html')

@app.route('/login')
def login():
    return render_template('userlogin.html')

@app.route('/xserver')
def xserver():
    return render_template('xservser.html')


app.run(port=5009)






