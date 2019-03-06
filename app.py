#!/usr/bin/env python
"""
Program: app.py
Purpose: Used for running Supermarket optimization tool
Author:  Sharad Varshney
Created: Jan 29th, 2019
"""
import logging
from optparse import OptionParser

from supermarket_optimization import SupermarketOptimization


if __name__ == "__main__":
    #if needed we can create a microservice out of this by adding micro webserver Flask here.
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    apriori = SupermarketOptimization()
    default_filename = './sample.dat'
    default_support = 4.0
    default_output = './frequent_sets_25K_new.txt'

    parser = OptionParser(usage="Program usage: %prog -f filename -s minimum support")
    filename, minsupport, output = SupermarketOptimization.get_inputs_from_cmd(parser,
                                        default_filename,default_support, default_output)


    dataset = apriori.load_data(filename)
    scanned_reduced_list, support_data = apriori.apriori_run(minsupport)
    logging.debug('Write output of the run to output file')
    SupermarketOptimization.write_output(scanned_reduced_list, support_data, output)
    
