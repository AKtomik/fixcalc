# tricks to replace strings inside strings


replace_shortcuts = {
    #syntax
# "from": "to",
    #shortcut
    "**": "^",
    #constants
    "e": "2.71828182845904523536",
    "E": "2.71828182845904523536",
    "π": "3.14159265358979323846",
    "PI": "3.14159265358979323846",
    "pi": "3.14159265358979323846",
    "pI": "3.14159265358979323846",
    "Pi": "3.14159265358979323846",
    "SIPI": "3",
    "sipi": "3",
    "sie": "3",
    "SIE": "3",
    #letters
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eigth":"8",
    "nine":"9",
    "ten":"10",
}


pow_to_digits = {
	"⁰":"0",
	"¹":"1",
	"²":"2",
	"³":"3",
	"⁴":"4",
	"⁵":"5",
	"⁶":"6",
	"⁷":"7",
	"⁸":"8",
	"⁹":"9",
	"⁻":"-",
	"˙":".",
}

def string_human_shortcut(string: str):

		#replace
    for k in replace_shortcuts.keys():
        string=string.replace(k, replace_shortcuts[k])
    new_string=""
    last_was_pow=False

		#unpower
    for char in string:
        powdigit=pow_to_digits.get(char)
        is_pow=(powdigit!=None)
        if is_pow:
            if (not last_was_pow):
                new_string+="^"
            new_string+=powdigit
        else:
            new_string+=char
        last_was_pow=is_pow
    return new_string

# derivate using replace method

derivatives_string = {
    "constant": "0",
    "x": "1",
    "x^n": "n*x^(n-1)",
    "1/x": "-1/x^2",
    "sqrt(x)": "1/(2*sqrt(x))",
    "cos(x)": "-sin(x)",
    "sin(x)": "cos(x)",
    "u+v": "u' + v'",
    "u*v": "u'*v + u*v'",
    "u/v": "(u'*v - u*v') / v^2",
    "v(u(x))": "(v'(u(x))) * u'(x)",
    "e^(u(x))": "u'(x) * e^(u(x))",
    "sqrt(u(x))": "u'(x) / (2*sqrt(u(x)))",
    "(u(x))^n": "n * u'(x) * u(x)^(n-1)",
    "cos(u(x))": "-u'(x) * sin(u(x))",
    "sin(u(x))": "u'(x) * cos(u(x))"
}

def simplify_expression(expr):
    """
    Simplifie quelques expressions mathématiques courantes.
    
    Args:
        expr (str): Expression à simplifier
        
    Returns:
        str: Expression simplifiée
    """
    # Remplacer les patterns courants
    # Coefficients 1
    expr = expr.replace("1*", "")
    
    # Traitement des négations multiples
    if "--" in expr:
        expr = expr.replace("--", "")
    
    # Simplifier x^1 en x
    expr = expr.replace("^1", "")
    
    # Simplifier les parenthèses inutiles
    if expr.startswith("(") and expr.endswith(")") and expr.count("(") == 1:
        expr = expr[1:-1]
    
    return expr

def derive(expression, variable='x'):
    """
    Dérive une expression mathématique simple en utilisant le dictionnaire de règles de dérivation.
    
    Args:
        expression (str): L'expression à dériver
        variable (str): La variable par rapport à laquelle dériver (par défaut 'x')
    
    Returns:
        str: L'expression dérivée
    """
    # Supprimer les espaces excédentaires
    expression = expression.strip()
    
    # Cas de base
    if expression == variable:
        return "1"
    
    # Vérifier si c'est une constante (nombre)
    try:
        float(expression)
        return "0"    # La dérivée d'une constante est 0
    except ValueError:
        pass
    
    # Chercher dans le dictionnaire de dérivées
    for pattern, derivative in derivatives_string.items():
        # Cas spécifiques
        if pattern == "x^n" and "^" in expression:
            parts = expression.split("^")
            if parts[0].strip() == variable:
                try:
                    n = float(parts[1].strip())
                    # Cas particuliers pour simplifier
                    if n == 0:
                        return "0"    # x^0 = 1, donc dérivée = 0
                    elif n == 1:
                        return "1"    # x^1 = x, donc dérivée = 1
                    elif n == 2:
                        return f"2*{variable}"    # Simplification pour x²
                    else:
                        # Simplifier x^(n-1) quand n-1 = 1
                        if n-1 == 1:
                            return f"{n}*{variable}"
                        else:
                            return f"{n}*{variable}^{n-1}"
                except ValueError:
                    pass
        
        # Opérations de base (+, -, *, /)
        if pattern == "u+v" and "+" in expression and not (expression.startswith("(") and expression.endswith(")")):
            terms = expression.split("+")
            u, v = terms[0].strip(), terms[1].strip()
            du, dv = derive(u, variable), derive(v, variable)
            
            # Simplification
            if du == "0" and dv == "0":
                return "0"
            elif du == "0":
                return dv
            elif dv == "0":
                return du
            else:
                return simplify_expression(f"{du} + {dv}")
        
        if pattern == "u*v" and "*" in expression and not (expression.startswith("(") and expression.endswith(")")):
            terms = expression.split("*")
            u, v = terms[0].strip(), terms[1].strip()
            du, dv = derive(u, variable), derive(v, variable)
            
            # Simplification
            if du == "0" and dv == "0":
                return "0"
            elif du == "0":    # 0*v + u*dv = u*dv
                try:
                    float_u = float(u)    # Si u est une constante
                    if float_u == 0:
                        return "0"
                    elif float_u == 1:
                        return dv
                    else:
                        return simplify_expression(f"{u}*{dv}")
                except ValueError:
                    return simplify_expression(f"{u}*{dv}")
            elif dv == "0":    # du*v + u*0 = du*v
                try:
                    float_v = float(v)    # Si v est une constante
                    if float_v == 0:
                        return "0"
                    elif float_v == 1:
                        return du
                    else:
                        return simplify_expression(f"{v}*{du}")
                except ValueError:
                    return simplify_expression(f"{du}*{v}")
            else:
                if u == v:    # Cas spécial: x*x = x²
                    if u == variable:
                        return f"2*{variable}"
                return simplify_expression(f"{du}*{v} + {u}*{dv}")
        
        if pattern == "u/v" and "/" in expression and not (expression.startswith("(") and expression.endswith(")")):
            terms = expression.split("/")
            u, v = terms[0].strip(), terms[1].strip()
            du, dv = derive(u, variable), derive(v, variable)
            
            # Simplification
            if du == "0" and dv == "0":
                return "0"
            elif du == "0":    # (0*v - u*dv)/v² = -u*dv/v²
                return simplify_expression(f"-{u}*{dv}/{v}^2")
            elif dv == "0":    # (du*v - u*0)/v² = du*v/v² = du/v
                return simplify_expression(f"{du}/{v}")
            else:
                return simplify_expression(f"({du}*{v} - {u}*{dv})/{v}^2")
            
        # Fonctions trigonométriques
        if pattern == "sin(x)" and expression == "sin(x)":
            return "cos(x)"
            
        if pattern == "cos(x)" and expression == "cos(x)":
            return "-sin(x)"
            
        # Fonction composée
        if pattern == "sin(u(x))" and expression.startswith("sin(") and expression.endswith(")"):
            u = expression[4:-1]    # Extraire u(x) de sin(u(x))
            du = derive(u, variable)
            
            # Simplification
            if du == "0":
                return "0"
            elif du == "1":
                return f"cos({u})"
            else:
                return simplify_expression(f"{du}*cos({u})")
            
        if pattern == "cos(u(x))" and expression.startswith("cos(") and expression.endswith(")"):
            u = expression[4:-1]    # Extraire u(x) de cos(u(x))
            du = derive(u, variable)
            
            # Simplification
            if du == "0":
                return "0"
            elif du == "1":
                return f"-sin({u})"
            else:
                return simplify_expression(f"-{du}*sin({u})")
                
        # Racine carrée
        if pattern == "sqrt(u(x))" and expression.startswith("sqrt(") and expression.endswith(")"):
            u = expression[5:-1]    # Extraire u(x) de sqrt(u(x))
            du = derive(u, variable)
            
            # Simplification
            if du == "0":
                return "0"
            elif du == "1":
                return f"1/(2*sqrt({u}))"
            else:
                return simplify_expression(f"{du}/(2*sqrt({u}))")
    
    # Gestion des expressions entre parenthèses
    if expression.startswith("(") and expression.endswith(")"):
        return derive(expression[1:-1], variable)
    
    # Si aucune règle ne correspond, retourner l'expression non dérivée avec une note
    return f"({expression})"

