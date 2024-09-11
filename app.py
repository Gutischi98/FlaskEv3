from flask import Flask, render_template, request
from calculos import promedio

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/notas', methods=['GET', 'POST'])
def notas():
    resultado = None
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asist = int(request.form['asistencia'])

        avg = promedio(nota1, nota2, nota3)

        if avg >= 40 and asist >= 75:
            resultado = f'Tu promedio es {avg} y tienes excelente asistencia, estás APROBADO! 😁'
        elif avg < 40 and asist >= 75:
            resultado = f'Tu promedio es {avg}, aunque tengas excelente asistencia REPRUEBAS 😢'
        elif avg >= 40 and asist < 75:
            resultado = f'Tu promedio es {avg}, pero no vienes nunca 😡. REPROBADO! 😡'
        elif avg < 40 and asist < 75:
            resultado = f'No se que explicaciones quieres. Promedio: {avg} y asistencia de: {asist}% 😒, pasar no es magico. REPROBADO! 😡😒'

    return render_template('formCalculadora.html', resultado=resultado)


@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    resNombre = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        lenNom1 = len(nombre1)
        lenNom2 = len(nombre2)
        lenNom3 = len(nombre3)

        if lenNom1 > lenNom2 and lenNom1 > lenNom2:
            resNombre = f'El nombre {nombre1} es el más largo, con un conteo de {lenNom1} letras.'
        elif lenNom2 > lenNom1 and lenNom2 > lenNom3:
            resNombre = f'El nombre {nombre2} es el más largo, con un conteo de {lenNom2} letras.'
        elif lenNom3 > lenNom1 and lenNom3 > lenNom2:
            resNombre = f'El nombre {nombre3} es el más largo, con un conteo de {lenNom3} letras.'
        elif lenNom1 == lenNom2 == lenNom3:
            resNombre = f'Los nombres {nombre1}. {nombre2} y {nombre3}, tienen la misma cantidad de letras, contando {lenNom1} en cada una.'
        elif lenNom1 == lenNom2 and lenNom1 > lenNom3:
            resNombre = f'Los nombres {nombre1} y {nombre2}, son igual de largos, contando {lenNom1} letras en cada uno, dejando a {nombre3} como el nombre mas corto.'
        elif lenNom2 == lenNom3 and lenNom2 > lenNom1:
            resNombre = f'Los nombres {nombre2} y {nombre3}, son igual de largos, contando {lenNom2} letras en cada uno, dejando a {nombre1} como el nombre mas corto.'
        elif lenNom1 == lenNom3 and lenNom1 > lenNom2:
            resNombre = f'Los nombres {nombre1} y {nombre3}, son igual de largos, contando {lenNom1} letras en cada uno, dejando a {nombre2} como el nombre mas corto.'

    return render_template('nombres.html', resultadoNombre=resNombre)


if __name__ == '__main__':
    app.run()
