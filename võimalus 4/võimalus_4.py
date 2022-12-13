#2
from math import*
from random import*
a=''
i=0
while a !=0:
    a = int(input("Sisestage number:" ))
    if a< 0:
       i += 1
print("Negatiivsete arvude arv:" + str(i))

#1
a, b = map(float, input().split())             	
if a > b:           	
    M = a     
else:                  	
    M = b           	
print("Maximum", M) 
    