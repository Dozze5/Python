import time
import math

num1 = int((input()))
num2 = int((input()))

t0 = time.time()

if(num1 == 1):
    num1 = 2

for num in range(num1,num2+1):
    for j in range(2,num):
        if num%j == 0:
            break
    else:
       print(num,end=",")
t1 = time.time()
print("\n\nTime required :", t1 - t0)



# # ---------------------------------------------------------------------------- #
# #                                Square Root Wat                               #
# # ---------------------------------------------------------------------------- #



num1 = int((input()))
num2 = int((input()))
t0 = time.time()

if(num1 == 1):
    num1 = 2
for i in range(num1 , num2):
    max_div = math.floor(math.sqrt(i))
    for j in range(2,max_div+1):
        if i%j == 0:
            break
    else:
        print(i,end=",")
        
t1 = time.time()
print("\n\nTime required :", t1 - t0)


# ---------------------------------------------------------------------------- #
#                               Only Odd Checking                              #
# ---------------------------------------------------------------------------- #

num1 = int((input()))
num2 = int((input()))


t0 = time.time()
if num1==2 or num1 == 1 or num1<1:
    print(2,end=",")

num1 = (lambda x : x+1 if x%2==0 else x)(num1)


for i in range(3,num2+1,2):
    if i > 1:
        for n in range(3,i,2):
            if i%n==0:
                break
        else:
            print(i,end=",")

t1 = time.time()
print("\n\nTime required :", t1 - t0)


# ---------------------------------------------------------------------------- #
#                                More Optimized                                #
# ---------------------------------------------------------------------------- #


num1 = int((input()))
num2 = int((input()))

t0 = time.time()

if num1==2 or num1 == 1 or num1<1:
    print(2,end=",")

num1 = (lambda x : x+1 if x%2==0 else x)(num1)



for i in range(num1,num2,2):
    if i>1:
        max_div = math.floor(math.sqrt(i))
        for j in range(3,max_div+1,2):
            if i%j == 0:
                break
        else:
            print(i,end=",")
            
t1 = time.time()
print("\n\nTime required :", t1 - t0)


# ---------------------------------------------------------------------------- #
#                                 Seive Method                                 #
# ---------------------------------------------------------------------------- #

num = int(input())

prime = []

for i in range(num+1):
    prime.append(i)
    
prime[0] =0
prime[1] =0
p =2
while(p*p<=num):
    if p != 0:
        for j in range(p*2,num+1,p):
            prime[j] = 0
    p += 1


for i in range(len(prime)):
    if prime[i] != 0:
        print(prime[i],end=",")