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

