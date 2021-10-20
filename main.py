from flask import Flask

app = Flask(__name__)

# lembrar de criar aruqivo config.py
# com as seguintes configurações
# SECRET_KEY = 'coloca qualquer coisa'
app.config.from_pyfile('config.py')


from views import *
if __name__ == '__main__':
    app.run(debug=True)
