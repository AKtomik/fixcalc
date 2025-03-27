# in this file : Flask UI to use calcul and derive.

from flask import Flask, request, render_template
from fixcalc import calcul, derive
from resluts import FractionResult ,RoundResult, Sett
from replace import express_style

from sys import platform, version

app = Flask(__name__)
stc = -1
def vr(t):
    if t == 'fraction':
        stc = 1
        return Sett.set_type_class(FractionResult)
    elif t == 'decimal':
        stc = 0
        return Sett.set_type_class(RoundResult)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None, resulttype=None, expressed=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    v = request.form.get('v', 'decimal')  # Default to decimal if not specified
    vr(v)
    if (not expression):
        return render_template('index.html', cbouton = stc, result=None, error=None, resulttype=v, expressed=None)
    
    expressed = express_style(expression)

    try:
        result = calcul(expression)
        print(result)
        return render_template('index.html', result=result, error=None, resulttype=v, expressed=expressed)
    except Exception as e:
        error_message = str(e) if str(e) else "Invalid expression"
        return render_template('index.html', result=None, error=error_message, resulttype=v, expressed=expressed)

@app.route('/example', methods=['POST'])
def example():
    return render_template('example.html', resulttype=None )

@app.route('/derivatives')
@app.route('/derivatives', methods=['POST'])
def derivatives():
    return render_template('derivatives.html', result=None, error=None, resulttype=None, expressed=None)

@app.route('/derivativescalculate', methods=['POST'])
def calculate_derivatives():
    expression = request.form.get('expression')
    expressed = express_style(expression)
    v = request.form.get('v', 'decimal')  # Default to decimal if not specified
    vr(v)

    try:
        # Could be added in the future :
        #Sett.set_use_unit(True)
        #Sett.set_derivate_by("xyztXYZT")
        # Pass the expression to the derive function
        result = derive(expression)
        return render_template('derivatives.html', result=result, error=None, resulttype=v, expressed=expressed)
    except Exception as e:
        error_message = str(e) if str(e) else "Expression invalide"
        return render_template('derivatives.html', result=None, error=error_message, expressed=expressed)

if __name__ == '__main__':
    print(f"launch fixcalc's index from platfrom [{platform}] version [{version}]...")
    if ('linux' in platform):
        print("this is a server. launching serverhost...")
        app.run(debug=True, host="0.0.0.0", port="12345")#serverhost
    else:
        print("this is a client. launching localhost...")
        app.run(debug=True, host="127.0.0.1", port="5000")#localhost