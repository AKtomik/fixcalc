from flask import Flask, request, render_template
from calculate import calcul 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    print(expression)
    try:
        result = calcul(expression)  
        return render_template('index.html', result=result, error=None)
    except Exception as e:
        return render_template('index.html', result=None, error="Invalid expression")
@app.route('/exmeple', methods=['POST'])
def index():
    return render_template('index.html', result=None, error=None)
if __name__ == '__main__':
    app.run(debug=True)
