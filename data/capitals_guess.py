#state capital guessing game

import random
import sys

state_capitals={"Washington":"Olympia",
		"Oregon":"Salem",
		"California":"Sacramento",
		"Ohio":"Columbus",
		"Nebraska":"Lincoln",
		"Colorado":"Denver",
		"Michigan":"Lansing",
		"Massachusetts":"Boston",
		"Florida":"Tallahassee",
		"Texas":"Austin",
		"Oklahoma":"Oklahoma City",
		"Hawaii":"Honolulu",
		"Alaska":"Juneau",
		"Utah":"Salt Lake City",
		"New Mexico":"Sante Fe",
		"North Dakota":"Bismarck",
		"South Dakota":"Pierre",
		"West Virginia":"Charleston",
		"Virginia":"Richmond",
		"New Jersey":"Trenton",
		"Minnesota":"Saint Paul",
		"Indiana":"Indianapolis",
		"Kentucky":"Frankfort",
		"Tennessee":"Nashville",
		"Georgia":"Atlanta",
		"Alabama":"Montgomery",
		"Mississippi":"Jackson",
		"North Carolina":"Raleigh",
		"South Carolina":"Columbia",
		"Maine":"Augusta",
		"Vermont":"Montpelier",
		"New Hampshire":"Concord",
		"Connecticut":"Hartford",
		"Rhode Island":"Providence",
		"Wyoming":"Cheyenne",
		"Montana":"Helena",
		"Kansas":"Topeka",
		"Iowa":"Des Moines",
		"Pennsylvania":"Harrisburg",
		"Maryland":"Annapolis",
		"Missouri":"Jefferson City",
		"Arizona":"Phoenix",
		"Nevada":"Carson City",
		"New York":"Albany",
		"Wisconsin":"Madison",
		"Delaware":"Dover",
		"Idaho":"Boise",
		"Arkansas":"Little Rock",
		"Louisiana":"Baton Rouge"
		}
		



#fhw = open('state_capital.txt','w')

'''
for key in state_capitals:
	fhw.write(key)
	fhw.write(',')
	fhw.write(state_capitals[key])
	fhw.write("\n")
'''	
	
	
	
state_list= list(state_capitals.keys())
t = list(state_capitals.keys())

#for i in state_list: 
#    print(i)

'''
for i in range(0,5):
    state = random.choice(state_list)
    capital = state_capitals[state]
    capital_guess = input("What is the capital of " + state +"? ")

    if capital_guess.lower() == capital.lower():
        print("Well done!!...You are correct!\n")
    else:
        print("Nope...The Capital of " + state +" is: " + capital+"\n")
    

print("All done")
random.shuffle(state_list)
'''

user_choice = input("Please press ENTER to continue to the game or type QUIT to exit  ").lower()


while user_choice != 'quit':
    state = random.choice(state_list)
    capital = state_capitals[state]
    capital_guess = input("What is the capital of "+ state +"? ")
    
    if capital_guess.lower() == capital.lower():
        print("Well done!!....You are correct!\n")
    elif capital_guess.lower() == 'quit':
        break
    else:
        print("Nope...The capital of "+ state +" is "+ capital+ "\n")
    


print("All done!!")
random.shuffle(state_list)








