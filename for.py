#mulitiplication table
n =int(input("enter the num: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


#sum of num
digits =[5,13,8,24,2]
sum=0
for digit in digits:
    sum += digit
print("sum of the digits:" ,sum)


#factorial 
m =int(input("enter the num: "))
fact = 1
for i in range(1,m+1):
    fact = fact*i
print("the factorial of the num is: ",fact)


#fibonacci series
n1 = 0
n2 = 1
count = 10

for i in range(2, count):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print(n3)

#prime
num =int(input("enter the number to be checked: "))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("The given num is not a prime num")
            break
    else:
        print("The given num is a prime num")
else:
    print("The given num is not a prime num")
    