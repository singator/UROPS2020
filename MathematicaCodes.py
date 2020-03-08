#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:13:10 2020

@author: wenhan
"""

import wolframclient.evaluation
from wolframclient.language import wl
from wolframclient.language import wlexpr

session=wolframclient.evaluation.WolframLanguageSession()
out1 = session.evaluate('Simplify[4x+1x==11, 5x==11]')
print(out1)

### convert latex form to mathematica form. Takes too long, does not end.
### Function works well when used directly on Mathematica.
out2 = session.evaluate(wl.ToExpression("\\frac{1}{11}", wlexpr('TeXForm')))
print(out2)

session.terminate()
