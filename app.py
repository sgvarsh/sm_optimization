#!/usr/bin/env python
"""
Program: app.py
Purpose: Used for running assignment model and smart routing
Author:  Sharad Varshney
Created: Jan 29th, 2019
"""
import logging
from supermarket_optimization import SupermarketOptimization

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s|%(asctime)s|%(filename)s -> %(funcName)s[%('
                               'lineno)d] |%(name)s|%(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    apriori = SupermarketOptimization()
    filename = './retail_25k.dat'
    filename = './sample.dat'
    minsupport = 4.0

    list = [[1, 2], [3, 2]]
    c1 = map(frozenset, list)
    for key, value in c1:
        print(key)
        print(value)
        print('New line')
    data = apriori.load_data(filename)
    run = apriori.apriori_run()
    logging.debug('FInalize the run')





