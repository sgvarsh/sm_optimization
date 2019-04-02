# Supermarket Optimization
Class for supermarket optimization using association which is typically used for market-basket
analysis, objective would be to locate trends within the data i.e. technique will attempt to find
groups of items that are commonly found together and thus can be used to determine which items can be placed together in
supermarket.

## How to run

**python3 app.py -f './retail_25k.dat' -s 4 -o ./frequent_sets_25K.txt**

-f is the filename of Transaction database
-s is the support level = 4
-o is where we will store our output

or we can also run simple as **python3 app.py** without any command line parameters.

## Several optimizations can be done on this code:
1. It tries to find frequent sets by running itertools.combinations under O(n^2) loop, this can definitely be optimized
2. Also can implement reduce candidate list 

### Ref
https://www.researchgate.net/publication/233754781_Support_vs_Confidence_in_Association_Rule_Algorithms
https://adataanalyst.com/machine-learning/apriori-algorithm-python-3-0/


