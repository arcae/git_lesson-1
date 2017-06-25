#Generic guessing game that takes input from a comma separated file passed as a argument
#format of input file is: ques,ans

import sys
import random

if len(sys.argv) < 2:
    print("Please enter input file as argument to script")
    exit(1)
    

f = open(sys.argv[1],'r',encoding = 'latin-1')

ques_ans={}
questions = []
answers = []

for line in f:
    line = line.strip().split(',')
    #print(line)
    questions.append(line[0])
    answers.append(line[1])
    ques_ans[line[0]] = line[1]

#print(questions)
#print(answers)
#print(ques_ans)
print("Press ENTER to start the quiz or QUIT to exit")


while True:
    ques = random.choice(questions)
    print("What is the capital of? " + ques)
    ans = input(">...")
    
    if ans.lower() == 'quit':
        print("Quitting the game now......Bye!")
        exit(1)
    elif ques_ans[ques].lower() == ans.lower():
        print("Well done!!")
    else:
        print("Nope....please try next question")
        print("The answer is " + ques_ans[ques])
        



print("Bye!! All done!!")
        
        
    
    


    
    
    