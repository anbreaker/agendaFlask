from flask import Flask, render_template, request

app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def hola():
    return render_template('agenda.html')


@app.route(r'/agregar', methods=['GET', 'POST'])
def agregar_contacto():
    
    if request.form:
        print(request.form.get('nombre'))
        print(request.form.get('movil'))
        print(request.form.get('mail'))
    
    return render_template('agregar_contacto.html')



if __name__ == '__main__':
    app.run()