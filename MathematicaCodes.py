#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:13:10 2020

@author: wenhan
"""

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
from wolframclient.language import wlexpr

session=WolframLanguageSession()


out1 = session.evaluate('Simplify[4x+1x==11, 11x==11]')
print(out1)
#out2 = session.evaluate('ToExpression["\\frac{1}{11}", TeXForm]')
#print(out2)
out2 = session.evaluate(wl.ToExpression('\\frac{1}{11}', wlexpr('TeXForm')))
print(out2)

session.terminate()
