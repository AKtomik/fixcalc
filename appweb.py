# in this file : Flask UI to use calcul and derive.

from flask import Flask, request, render_template
from fixcalc import calcul, derive
from resluts import FractionResult ,RoundResult, Sett

app = Flask(__name__)

def vr(t):
    if t:
        return Sett.set_type_class(FractionResult)
    else :
        return Sett.set_type_class(RoundResult)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    v = 'v' in request.form 
    vr(v)

    if (not expression):
        return render_template('index.html', result=None, error=None)

    try:
        result = calcul(expression)
        print(result)
        return render_template('index.html', result=result, error=None)
    except Exception as e:
        error_message = str(e) if str(e) else "Invalid expression"
        return render_template('index.html', result=None, error=error_message)

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
    v = 'v' in request.form 
    vr(v)
    variable = request.form.get('variable', 'x')  # Default to 'x' if not provided
    
    # Validate that variable is a single character
    if len(variable.strip()) != 1:
        return render_template('derivatives.html', result=None, error="La variable doit être un seul caractère", expression=expression, variable=variable)
    
    try:
        # Could be added in the future :
        #Sett.set_use_unit(True)
        #Sett.set_derivate_by("xyztXYZT")
        # Pass the variable to the derive function
        result = derive(expression)
        return render_template('derivatives.html', result=result, error=None, expression=expression, variable=variable)
    except Exception as e:
        error_message = str(e) if str(e) else "Expression invalide"
        return render_template('derivatives.html', result=None, error=error_message, expression=expression, variable=variable)

if __name__ == '__main__':
    app.run(debug=True)
