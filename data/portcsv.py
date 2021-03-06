#using csv module

import csv

def portfolio_cost(filename):
	'''
	Computes total shares*proce for a CSV file with name,shares,price data'
	'''

	total = 0.0

	with open(filename,'r') as f:
		rows = csv.reader(f)
		headers = next(rows)    #skip first row for headers
		for rowno, row in enumerate(rows,start=1):
			try:
				row[2] = int(row[2])
				row[3] = float(row[3])
			except ValueError as err:
				print('Row:',rowno, 'Bad row:',row)
				print('Row:',rowno, 'Reason:', err)
				continue #skip to the next row
		total += row[2]*row[3]

	return total


total = portfolio_cost('Mydata1.csv')
print('Total cost:', total)


