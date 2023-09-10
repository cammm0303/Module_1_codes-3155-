import time
import random
 
#Fib. Function:
#if the number is 1 return it as it is.
def fibonacci(n):
  if n <= 1:
    return n
  #T1 and t2 are place holders to transfer the sequence to the next term.
  t1 = 0
  t2 = 1
  for i in range(2,n+1):
    next_term = t1 + t2
    t1 = t2
    t2 = next_term
  return next_term
 
#this is the main code where the "fibonacci" fuction is called and utilized 
#I track the time by subtracting the time of the finish by the time we start to find the diffrence:
#n is set to a random number to send to the fib. function
t1 = time.time()
n = random.randint(15,30)
res = fibonacci(n)                            
t2 = time.time()                              

#Prints:
print ("Fibonacci("+ str(n) +") = "+ str(res))
print ("Time taken =", t2 - t1)