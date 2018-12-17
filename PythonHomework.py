
# coding: utf-8

# In[116]:


#WHEN YOU RUN THIS THERE WILL BE NO OUTPUT. DRIVERS ARE COMMENTED OUT UNDER THEIR RESPECTIVE METHODS


#exercise 5
x = 11
found = 0

while(found <= 20):
    if (x % 11 == 0 and x % 7 == 0 and x % 5 == 0):
        #print(x)  #UNCOMMENT TO PRINT OUTPUT
        found += 1
    x += 1
# prints 385   770   1155   1540   1925   2310   2695   3080   3465   3850
#     4235   4620   5005   5390   5775   6160   6545   6930   7315   7700   8085



#exercise 6a
def is_prime(n):     
    if (n==1):
        return False 
    if (n==2):
        return True
    else:
        for x in range(2,n):
            if (n % x==0):
                return False
        return True
#is_prime(31) example


#exercise 6b
def is_prime(n):     
    if (n==1):
        return False
    if (n==2):
        return True
    if (n==3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        x = 5
        while(x*x <= n):
            if(x % (x + 2) == 0 or n % x == 0):
                return False
            x += 6
        return True
#is_prime(31) example


#exercise 6c
def returnupto(n):        #iterates from 0 to n value, calling is_prime
    currentvalue = 0
    while(currentvalue <= n):
        if(is_prime(currentvalue) == True):
            print(currentvalue)
        currentvalue += 1 
        
def is_prime(n):          #prime function from before
    if (n==1):
        return False
    if (n==2):
        return True
    else:
        for x in range (2,n):
            if(n%x == 0):
                return False
        return True
#returnupto(100) #example 


#exercise 6d
def is_prime(n):    #sees if number given is prime 
    if (n==1):
        return False
    if (n==2):
        return True
    if (n==3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        x = 5
        while(x*x <= n):
            if(x % (x + 2) == 0 or n % x == 0):
                return False
            x += 6
        return True
    
def giveupton(n):        #iterates until nth number, calling is_prime
    primesfound = 0
    number = 0
    counter = 1
    while(primesfound < n):
        
        if(is_prime(number) == True):
            
            print("Prime number ",counter, ":", number)
            primesfound += 1
            counter += 1
            
        number += 1
        
#giveupton(100)


#exercise 7a
def printList(list = []):
        print(list)
        
a = [1,2,3,4,5]
#printList(a)


#exercise 7b
def printList(list = []):
        list.reverse()
        print(list)
        
a = [1,2,3,4,5]
#printList(a)


#exercise 7c
def countList(list = []):
    increments = 0
    for i in list:
        increments += 1
        
    return increments

a = [1,2,3,4,5,6,7,8]
#countList(a)


#exercise 8
a = [1,2,3,4,5]
b = a
b[1] = 9
c = a[:]
c[2] = 8

#print(a)
#print(b)
#print(c)


def set_first_elem_to_zero(list = []):
    list[0] = 0
    return list

set_first_elem_to_zero(a)
#print(a)
#print(b)
#print(c)

#exercise 9
x = [[1,3], [4,6]]

subcombined = sum(x, [])
#print(subcombined)


#exercise 10
import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0,2,0.01)
#y = (np.sin(x-2)**2)*np.exp(-x**2)
#plt.plot(x,y)

#plt.title("sin(x-2)^2*e^(-x^2) along the increment of 0-2.", fontsize=12)
#plt.xlabel("0-2")
#plt.ylabel("sin(x-2)^2*e^(-x^2)")


#exercise 11
def iteration(l = []):
    i = 0
    result = 0
    while(i < len(l)):
        result = result + l[i]
        i += 1
    return result

a = [1,2,3,4,5,6]	#adds up to 21
#print(iteration(a))


def recursion(l = []):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recursion(l[1:])

a = [2,4,6,8,10] #adds up to 30
#print(recursion(a))


#exercise 12
def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

#fibo(10) #example

    
#exercise 13
import re
def findemails() : 
        file=open("C:/Users/Jake Hiban/Desktop/PythonThings/emails.txt","r").read()
        found = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", file)
        print (found)
#findemails()

