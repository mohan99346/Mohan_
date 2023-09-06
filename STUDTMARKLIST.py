print(format("GRADE CALCULATION:",'^60'))

mylist=[212200428,212200429,212200430,212200431,212200432,212200433,212200434,212200435,]

studname=input("enter student name:")
studregno=int(input("ENTER STUDENT REGISTER NUMBER:"))

if studregno in mylist:
   print("valid number:")

else:
   print("REGISTER NUMBER NOT VALID")
   quit()
   
birthyear=int(input("enter birth of year only:"))

if birthyear >=2003 and birthyear <2007:
   print("YOUR BIRTH YEAR IS VALID")
else:

   print("YOUR BIRTH YEAR IS NOT VALID")
   
   quit()

   
print("enter your marks:")
#def studentmarklist():

 # tamil english maths python ss=<100:


    # print("invalid marks")

#def studmarklist()
tamil=int(input("TAMIL:"))
english=int(input("ENGLISH:"))
maths=int(input("MATHS:"))
python=int(input("PYTHON:"))
ss=int(input("SOFTSKILL:"))
if studmarklist=<100:
 print("studmarklist")
else:
    print("invalid marks")


studtotal=int(tamil+english+maths+python+ss)
print("student total marks:",studtotal)

studentmark=(tamil,english,maths,python,ss)


percentage=(studtotal) / len(studentmark)
Grade=''



if percentage >=80:
             Grade='A'
elif percentage >=70 and percentage <80:
    Grade ='B'
elif percentage >=60 and percentage <70:
    Grade='C'
elif percentage >=40 and percentage <60:
    Grade='D'
else:
    Grade='F'

print(format("prcentage;",'<20'),percentage)
print(format("Grade:",'<20'),Grade)
            
