#Palindrome

#word = input("Enter the word = ")
'''x1 = word[::-1]
if word == x1:
    print("Palindrome")
else:
    print("Not Palindrome")'''
    
    #Factorial
    
#import math

'''num = int(input("Enter the number = "))

f = math.factorial(num)

print(f)'''


    #Fibonnaci
    
'''a = int((input("enter the first number")))   
b = int(input('Enter the second nmber '))
n = int(input("Number of elemnt"))

print(a,b,"end")

while n-2:
    c=a+b
    a=b
    b=c
    
    print(c,"end")
    
    n=n-1    '''
    
    #armstrong
    
'''num = int(input("Enter the number"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10
    
    if num == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")  '''
        
        
        #pattern
'''n  = int(input("Enter the number  "))
for i in range(n):
    for j in range(n-i-1):
        print("",end="")
        for k in range(2*i+1):
            print("*",end="")
            print()'''
            
            
            #leapyear
            
'''year = int(input("Enter the currrent year"))

if year % 400 == 0:
 print("Leap")
elif year % 4 == 0:
 print("Leap")
 
elif year % 100 == 0:
    print("Not Leap")
else:
    print("not leap")'''
    
    #prime
    
'''num = int(input("Enter the Number"))    
 
for x in range(2,num):
 
 if num % x == 0:
     break
 if x+1 == num:
     print("Prime")    
else:
     print("not Prime")'''
     
     #Area Circle
     
#import math


'''pi = math.pi

cube = 6*side*side

cylinder = 2*pi*height + 2*pi*radius  
  
  circle = pi*(radius**2)   
  
  radius = 2*pi*(radius**2)
     
                
                
                
            
        '''