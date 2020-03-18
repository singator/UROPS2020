

import sympy

def check_expr_equality(priorExpr, posteriorExpr):
    if sympy.simplify(posteriorExpr - priorExpr) == 0:
        return True
    else:
        return False