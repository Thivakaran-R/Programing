if (True):
  print("yes")
else:
  print("no")

#NEXT PROGRAMING
meghna = input()
if(meghna == "Died"):
  print("surya meet priya")
else:
  print("Surya weds meghna")

#NEXT PROGRAMING
meghna = input("Meghna Died or Not : ")
if(meghna == "Died"):
  print("surya meet priya")
else:
  print("Surya weds meghna")
  
#NEXT PROGRAMING
mark= int(input("Enter the mark:"))
if(mark >=35):
  print("Pass")
else:
  print("Fail")

#NEXT PROGRAMING
income= int(input("Enter the Income :"))
if(income > 7000):
  print(" Not Eligible for scholarship")
else:
  print("Eligible for Scholarship")

#NEXT PROGRAMING
a= int(input())
if(a%3==0):
  print("Divisible by 3")
elif (a%5==0):
  print("Divisible by 5")
else:
  print("Not Divisible by 3 and 5")

#NEXT PROGRAMING

a= int(input())
if(a%3==0 and a%5==0):
  print("Divisible by 3 & 5")
else:
  print("Not Divisible by 3 and 5")

#NEXT PROGRAMING EVEN OR ODD

a= int(input("Enter Number: "))
if(a%2==0):
  print("This Even Num")
else:
  print("This Odd Num")

#NEXT PROGRAMING

a= int(input())
if(a>70 && a<100):
  print("Good Student")
elif(a>=35 and a<=70):
  print("Average Student")
elif(a<35):
  print("poor student")
else:
  print("Invalid")

#NEXT PROGRAMING ADD/SUB/MUL/DIV


a= int(input())
b= int(input())
c= input("ADD/SUB/MUL/DIV:")
if(c=="add"):
  print("Add:",a+b)
  
elif(c=="sub"):
  print("Sub:",a-b)
  
elif(c=="mul"):
  print("MUL",a*b)
  
elif(c=="div"):
  print("DIV:",a/b)
  
else:
  print("Invalid")