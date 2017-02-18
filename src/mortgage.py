#mortgage.py
#
#Find out how long to pay off the mortgage
#!/usr/bin/python3
import sys
principal = 114000
payment = 1356.36
rate = 0.0325
total_paid = 0

#Extra payment
extra_payment = 200
extra_payment_start_month = 1
extra_payment_end_month = 60
month=0

out = open('schedule.txt','w') #Open a file for writing output



print('{:<10s} {:<10s} {:<10s}{:<14s} {:<10s}'.format('Month','Interest','Principal','Total Payment','Remaining'),file=out)

while principal > 0:
   month += 1
   if month >= extra_payment_start_month and month <= extra_payment_end_month:
       total_payment = payment + extra_payment
   else:
       total_payment = payment
   interest = principal*(rate/12)
   #print('Interst is:',interest)
   principal = principal + interest - total_payment
   #print('Principal is:',principal)
   total_paid = total_paid + total_payment
   #print('total_paid:',total_paid)
   #print('+++++++++++++++++++++++')
   print('{:<10d} {:<10.2f} {:<10.2f}{:<14.2f} {:<10.2f}'.format(month, interest, total_payment-interest,total_payment, principal),file=out)

out.close()

print('Total paid:',total_paid)



