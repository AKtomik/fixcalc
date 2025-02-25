from flask import Flask, request, render_template
from calculate import calcul  
from Fraction import vr  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    v = 'v' in request.form 
    
    try:
        result = vr(calcul(expression),v)  
        print(result)
        return render_template('index.html', result=result, error=None)
    except Exception:
        return render_template('index.html', result=None, error="Invalid expression")

@app.route('/exmeple', methods=['POST'])
def example():
    return render_template('exmeple.html')  

if __name__ == '__main__':
    app.run(debug=True)
