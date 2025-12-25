#conditional statements
marks=890

if(marks>80):
    print("You Are Eligible")
elif(marks==80):
    print("You are pass")
else:
    print("You are not eligible")

#Grading
Marks=int(input("Enter your Marks:"))
if(Marks>=90):
    print("Grade A")
elif(Marks>=80):
    print("Grade B")
elif(Marks>=70):
    print("Grade C")    
else:
    print("Grade D")

#Practice Question
Num=int(input("Enter Number:"))
if(Num>0):
    print("Positive")
elif(Num==0):
    print("Zero")
elif(Num<0):
    print("Nrgative")