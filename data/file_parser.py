#Generic code to parse through a csv file


import sys
import random

#Check if filename is passed as argument to script, otherwise exit with message
if len(sys.argv) < 2:
    print("Please supply the filename")
    exit(1)
#Grab file name 
filename = sys.argv[1]
#print(sys.argv[0])
#print(sys.argv[1])

fh = open(filename, 'r')

# uncomment below to parse SS_2017Transactions.csv and send data to output.txt
'''
fw = open('output.txt', 'w')
for line in fh:
    line = line.strip().split(',')
    #print(line)
    fw.write(line[1] +"\t"+ line[0] +"\t" +line[3] +"\n")
'''    
# Stores data from csv file into lists

fw = open('nation_capital.txt','w')

ques_ans = {}
question = []
answer = []
for line in fh:
    line = line.strip()
    print(line)
    #line = line.strip().split(' ')
    #question.append(line[0])
    #answer.append(line[1])
    fw.write(line)
    fw.write('\n')
    line = line.split(',')
    ques_ans[line[0]] = line[1]
    question.append(line[0])
    answer.append(line[1])
    
    
print(ques_ans)
print(question)
print(answer)
print("The number of countries is " + str(len(question)))
    
    

    

    
    
    
'''    
#Store data from csv file into a dictionary and guess the answer
questions_ans = {}
for line in fh:
    line = line.strip().split(',')
    questions_ans[line[0]] = line[1]
    
questions = list(questions_ans.keys())
print('Type quit to exit anytime....')
while True:
    state = random.choice(questions)
    print(state + '?')
    user_ans = input(' >> ')
    
    if user_ans.lower() == questions_ans[state].lower():
        print('Well done!')
    
    elif user_ans.lower() == 'quit':
        break   
    else:
        print('Nope...The answer is ' + questions_ans[state])
 
'''       
        
    
    
    

    



    
    
                               

    








    
    
    


    
    



