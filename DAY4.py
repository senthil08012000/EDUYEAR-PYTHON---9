#occurance of y

count=0
string=input("enter the string")
for i in range(0,len(string)):
    if string[i]=="y":
        count+=1
print(count)
print()
print()
#even index characters
for i in range(0,len(string)):
    if(i%2==0):
        print(string[i])
print()
print()
#swapcase
j=0
while(j<len(string)):
    if(string[j].islower()):
        a=string[j].upper()
        print(a)
    else:
        b=string[j].lower()
        print(b)
    j+=1
    
    
    

