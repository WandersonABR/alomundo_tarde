#print("Hello World")
from flask import Flask, render_template
from matematica import Matematica
from timefut import TimeFut

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return  'Olá mundo! inicio'

@app.route('/pagina')
def mostrar():
    return  render_template('pagina.html')

@app.route('/calculosoma')
def calcular():
    mat = Matematica(5,7)
    resposta = mat.somar()
    return  render_template('calculo.html', resultado=resposta)

@app.route('/listatimes')
def listar_times():
    t1 = TimeFut('Palmeiras', 10)
    t2 = TimeFut('Botafogo', 7)
    t3 = TimeFut('Flamengo', 9)
    t4 = TimeFut('Vasco', 9)
    t5 = TimeFut('Curitiba', 11)
    t6 = TimeFut('Santos', 8)
    t7 = TimeFut('Corinthians', 15)
    t8 = TimeFut('Bragantino', 12)
    t9 = TimeFut('Atlético-MG', 6)
    t10 = TimeFut('São Paulo', 9)
    lista = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    return render_template('listatimes.html', times=lista)
    

app.run(debug=True)

