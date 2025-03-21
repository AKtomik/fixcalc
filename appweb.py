from flask import Flask, request, render_template
from calculate import calcul  
from resluts import FractionResult ,RoundResult 
from operators import derive
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

@app.route('/derivatives')
@app.route('/derivatives', methods=['POST'])
def derivatives():
    return render_template('derivatives.html', result=None, error=None, expression=None, variable='x')

@app.route('/derivativescalculate', methods=['POST'])
def calculate_derivatives():
    expression = request.form.get('expression')
    variable = request.form.get('variable', 'x')  # Default to 'x' if not provided
    
    # Validate that variable is a single character
    if len(variable.strip()) != 1:
        return render_template('derivatives.html', result=None, error="La variable doit être un seul caractère", expression=expression, variable=variable)
    
    try:
        # Pass the variable to the derive function
        result = derive(expression, variable.strip())
        return render_template('derivatives.html', result=result, error=None, expression=expression, variable=variable)
    except Exception as e:
        error_message = str(e) if str(e) else "Expression invalide"
        return render_template('derivatives.html', result=None, error=error_message, expression=expression, variable=variable)

if __name__ == '__main__':
    app.run(debug=True)
