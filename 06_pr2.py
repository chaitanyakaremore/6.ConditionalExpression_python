# stud1=int(input("Enter marks of student1:"))
# stud2=int(input("Enter marks of student2:"))
# stud3=int(input("Enter marks of student3:"))

# if(stud1>=35 and stud2>=35 and stud3>=35):
#     print("Pass")
# else:
#     print("Fail")

stud1=int(input("Enter marks of student1:"))
stud2=int(input("Enter marks of student2:"))
stud3=int(input("Enter marks of student3:"))

if(stud1<33 or stud2<33 or stud3<33):
    print("You are fail because you scored less than 33 mark in some subject")
elif(stud1+stud2+stud3)/3 < 40 :
    print("You are fail because you scored less than 40 percent in some subject")  
else:
    print("Congratulation!! you are pass.") 