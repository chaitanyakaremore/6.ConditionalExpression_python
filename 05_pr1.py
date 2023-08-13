# a=int(input("Enter number of a:"))
# b=int(input("Enter number of b:"))
# c=int(input("Enter number of c:"))
# d=int(input("Enter number of d:"))
# if (a>b and a>c and a>d):
#     print("Value of a is greater:")
# elif (b>a and b>c and b>d):
#      print("Value of b is greater:")
# elif (c>a and c>b and c>d):
#      print("Value of c is greater:")
# elif (d>a and d>c and d>b):
#      print("Value of d is greater:")
# else :
#      print("Done")

a=int(input("Enter number of a:"))
b=int(input("Enter number of b:"))
c=int(input("Enter number of c:"))
d=int(input("Enter number of d:"))

if(a>d):
    f1=a
else:
    f1=d

if(b>c):
    f2=b
else:
    f2=c    

if(f1>f2):
    print(str(f1)+"is grater")
else:
    print(str(f2)+"is grater")   

