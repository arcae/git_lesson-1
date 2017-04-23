#sscsv_category

import csv
import sys
from itertools import islice

cat_list = []
filename = sys.argv[1]

def populate_category(filename, item):
    cat_tot = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #print(item)
        #for item in cat_list:
        for row in rows:
            if row[0] == item:
                row[3] = float(row[3])
                cat_tot = cat_tot + row[3]
        #print("%s is: %f" %(item, cat_tot))
        print("{} total is: ${:.2f}".format(item, cat_tot))
        
            
def categories(filename):
    with open(filename, 'r') as f:
        rows = csv.reader(islice(f,6,None))
        #headers = next(rows)
        for row in rows:
            cat_list.append(row[0])
    return (set((cat_list)))
                    

def get_cat_total(cat_list):
    for item in cat_list:
        populate_category(filename, item)

    
    
        
        
cat_list = categories(sys.argv[1])       
#populate_category(sys.argv[1], cat_list)
get_cat_total(cat_list)

#print('The Net total is:${0:.3f}'.format(cat_total))

        