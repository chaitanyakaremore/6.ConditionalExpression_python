# marks= int(input("Enter the markes:"))
# if marks>90 and marks<100 :
#     print("Excilence")
# elif marks>80 and marks<90 :
#     print("grade A")
# elif marks>70 and marks<80 :
#     print("grade B")
# elif marks>60 and marks<70 :
#     print("grade C")
# elif marks>50 and marks<60 :
#     print("grade D")
# else:
#     print("grade f")

marks= int(input("Enter the markes:"))
if marks>=90:
    grade ="E"
elif marks>=80:
    grade ="A"
elif marks>=70:
    grade ="B"
elif marks>=60:
    grade ="C"
elif marks>=50:
    grade ="D"
else:
    grade ="F"
print("your grade is:"+grade)