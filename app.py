from flask import Flask

app = Flask(__name__)

#rota: http://google.com/search?q=iriniwe

@app.route('/')
def principal(): #método que é processado na rota anterior
	return '<h3>hello world</h3>'

app.run(port=5050)

#http://127.0.0.1:5000
#para executar, digite: 1. cd + caminho da pasta 2. python app.py 3. flask run 4. copiar http pro navegador.

