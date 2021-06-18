#create list
lst=[]
n=int(input("enter the no of element in list"))
for i in range(n):
    element=int(input("enter the elements"))
    lst.append(element)
print(lst)
print()
print()
#count of even and odd numbers
evencount=0
oddcount=0
for i in range(n):
    if(lst[i]%2==0):
        evencount+=1
    else:
        oddcount+=1
print("no of even numbers",evencount)
print("no of odd numbers",oddcount)
print()
print()
#max and min element
maximum=lst[0]
minimum=lst[0]
for i in range(n):
    if(lst[i]>=maximum):
        maximum=lst[i]
print("maximum is ",maximum)
for i in range(n):
    if(lst[i]<=minimum):
        minimum=lst[i]
print("minimum is ",minimum)
#list is palindrome or not
c=lst[::-1]

if(c==lst):
    print("list is a palindrome")
else:
    print("list is not palindrome")

print()
print()
#list element is palindrome
e=0
for i in range(n):
    b=str(lst[i])
    d=b[::-1]
    if(b==d):
        print("palindrome elements",b)
        e+=1
if(e<=0):
    print("no palindromes")

    



