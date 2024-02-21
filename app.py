from flask import Flask

app = Flask(__name__)

# localhost:5000/welcome


@app.get('/welcome')
def welcome():
    return 'welcome'

# localhost:5000/welcome/home


@app.get('/welcome/home')
def welcome_home():
    return 'welcome home'

# localhost:5000/welcome/back


@app.get('/welcome/back')
def welcome_back():
    return 'welcome back'
