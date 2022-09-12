# Write your code here :-)
from unicodedata import name


print ('Hello Beautiful Humans!')
print ('What is your name?') 
myName=input()

print ("Lovely to meet you new friend, "+myName)
theYear=2022

print('What is your age?')
yourAge=input()


print ("Awesome, you are: "+yourAge)

#print ('You were born in 'int(theYear-yourAge))

print(f"{'You were born in'} {theYear-int(yourAge)}")


