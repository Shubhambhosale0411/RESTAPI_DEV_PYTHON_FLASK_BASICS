from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
    return 'welcome this is home'

from controller import *
#import controller.user_controller as user_controller
#import controller.product_controller as product_controller



