a=int(input("Enter any number:"))
sum=0
b=a
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of it digit of {} is {}".format(b,sum))
