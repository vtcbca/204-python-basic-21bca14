num=int(input("Enter any Number:"))
c=num
s=0
while(num>0):
    r=num%10
    s=r+s*10
    num=num//10
if(c==s):
    print("{} is Palindrom number".format(c))
else:
    print("{} is not Plaindrom number".format(c))
