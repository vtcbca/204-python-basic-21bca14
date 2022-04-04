a=int(input("Enter any Number:"))
c=0
d=a
while(a>0):
    b=a%10
    c=c+b*b*b
    a=a//10
if(d==c):
    print("{} it is a armstrong number".format(c))
else:
    print("{} it is not anrmstrong number".format(c))
