#divisible by 5&7
n=int(input("enter the number"))
m=int(input("enter the number"))
for i in range(n,m+1):
    if(i%5==0 or i%7==0):
        print("divisible of 5 & 7:",i)
print()
print()
#series 2+22+222+2222+...+n
i=0
j=int(input("enter the no of terms"))
b=0
sum1=0
for i in range (0,j):
    b=b+(2*(10**i))
    sum1=sum1+b
    print("sum of the series:",sum1)
print()
print()
#factorial of the number
a=int(input("enter the number"))
fact=1
while a>0:
    fact=fact*(a)
    a=a-1
print("factorial:",fact)
print()
print()
#swap case
string=input("enter the string")
j=0
while(j<len(string)):
    if(j%2==0):
        a=string[j].upper()
        print(a)
        print("-")
    else:
        b=string[j].lower()
        print(b)
        print("-")
    j+=1
                                                                                                                   
