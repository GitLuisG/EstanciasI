from flask import Flask
from flask import Flask
from flask_restful import Resource, Api
from EstanciasI import *

app = Flask(__name__)

  
@app.route('/')

def index():
    return '<h1>Hello {}</h1>'.Conexion=ServicioGoogle()
