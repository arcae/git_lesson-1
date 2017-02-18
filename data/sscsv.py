# sscsv.py

import csv
import sys

def income_expense(filename):
    total = 0.0
    with open(filename,'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
          row[3] = float(row[3])
          total += row[3]
        return total


total = income_expense(sys.argv[1])
print('The Net total is:${0:.3f}'.format(total))


