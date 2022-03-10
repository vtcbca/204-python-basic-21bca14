n=int(input("Enter  any number:"))
for i in range(1,9):
    if(n%i==0):
        print("{} is divisible by {}".format(n,i))
