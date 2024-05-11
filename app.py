from flask import Flask
import random
import os 
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hola esta es una pagina donde puedes hacer diferentes cosas:</h1><a href="/contraseña">¡Generar una contraseña aleatoria!</a><br><br><a href="/imagen">¡Mostrar imagen aleatoria!</a>'

@app.route("/contraseña")
def contra():
    caracteres = ["+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    c = []
    for i in range(10):
        c += random.choice(caracteres)
    c1 = ''.join(c)
    return f"<p> La contraseña es: {c1}</p>"    


@app.route("/imagen")
def img():
    imagenes = os.listdir("img")
    i = random.choice(imagenes)
    return f"<img src='imagenes'/>"

app.run(debug=True)
