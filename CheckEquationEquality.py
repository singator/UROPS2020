import sympy

def check_eq_equality(priorExpr, posteriorExpr):
    if sympy.simplify(priorExpr >> posteriorExpr) == True:
        return True
    else:
        return False