from flask import Flask, request, render_template
from calculate import calcul  
from resluts import FractionResult ,RoundResult 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    v = 'v' in request.form 
    def vr(t):
        if t==True :
            return FractionResult
        else :
            return RoundResult

    try:
        result = calcul(expression,vr(v))
        print(result)
        return render_template('index.html', result=result, error=None)
    except Exception:
        return render_template('index.html', result=None, error="Invalid expression")

@app.route('/example', methods=['POST'])
def example():
    return render_template('example.html')

@app.route('/derivatives', methods=['POST'])
def derivatives():
    return render_template('derivatives.html')  
@app.route('/derivativescalculate', methods=['POST'])
def calculate_derivatives():

    try:
        return render_template('derivatives.html', result="result", error=None)
    except Exception:
        return render_template('derivatives.html', result=None, error="Invalid expression")

if __name__ == '__main__':
    app.run(debug=True)
