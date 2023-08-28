def evenorodd(msg):
  a=int(input(msg))
  if(a%2==0):
    print("Even")
  else:
    print("Odd")

evenorodd("Enter Number :")


def pass_or_fail(msg):
  
  if(msg>=35 and msg<=100):
    print("Pass")
  else:
    print("Fail")

a=int(input("Enter Number :"))
pass_or_fail(a) 


def pass_or_fail(a,b):
  for i in range(a,b):
    print(i)
  
a=int(input("Enter Number :"))
b=int(input("Enter Number :"))
pass_or_fail(a,b)