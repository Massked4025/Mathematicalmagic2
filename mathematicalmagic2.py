from math import sqrt
num = int(input("Enter your number: "))
if num > 1:
    for i in range(2, int(sqrt(num))+1):
        if num%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not prime")

#sieve of erasthothenes

def prime(n):
    list = [True for i in range(n+1)]
    currentnum = 2
    while(currentnum*currentnum<=n):
        if (list[currentnum]==True):
            for i in range(currentnum**2, n+1, currentnum):
                list[i]=False
        currentnum +=1
    list[0]=False
    list[1]=False
    for j in range(n+1):
        if list[j]:
            print(j)

n = int(input("Enter the last number: "))
prime(n)

#Printing between given range

a = 1000
for num in range(1, a+1):
    c = 0
    res = 0
    temp = num
    for i in range(1, temp+1):
        if temp%i==0:
            c+=1
    if c==2:
        while temp>0:
            res = res*10+(temp%10)
            temp//=10
        if res==num:
            print(num)