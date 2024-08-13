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
    lista = [t1,t2,t3]
    return render_template('listatimes.html', times=lista)
    

app.run(debug=True)

