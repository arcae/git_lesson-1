#port.py


total = 0.0
with open('Mydata1.csv','r') as f:
   headers = next(f)                #skip the first line for headers
   for line in f:
       line =line.strip()           #strip whitespace
       line = line.replace('/','-') #replace / with -
       parts = line.split(',')
       parts[2]=int(parts[2])
       parts[3]=float(parts[3])
       #print(parts)
       #print(line)
       total += parts[2]*parts[3]




print('Total cost is:',total)



