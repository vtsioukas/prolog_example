# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:12:25 2020

@author: vasilis
"""
from __future__ import print_function
from pyswip import Functor, Variable, Query, call

assertz = Functor("assertz", 1)
father = Functor("father", 2)
call(assertz(father("michael","john")))
call(assertz(father("michael","gina")))
X = Variable()

q = Query(father("michael",X))
while q.nextSolution():
    print("Hello,", X.value)
q.closeQuery()

# Outputs:
#    Hello, john
#    Hello, gina