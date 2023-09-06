

for i in "apple":
  print(i)
# NEXT PROGRAMMING 
for i in range(1,11):
  
  print(i,"*2=",i*2)

# NEXT PROGRAMMING 

a=int(input())
b=int(input())
for i in range(a+1,b):
  print(i)

# NEXT PROGRAMMING 

count=0
count1=0
for i in range(1,11):
  if(i%2==0):
    count=count+1
  elif(i%2==1):
    count1=count1+1
    
print("Even num conunt:",count)
print("Odd num conunt:",count1)

# NEXT PROGRAMMING 
count=0

for i in range(1,100):
  if(i%3==0 and i%5==0):
    count=count+1
print("DIV by 3 & 5 :",count)

# NEXT PROGRAMMING 
sum=0
for i in range(1,6):
  sum = sum+i
print(sum)

# NEXT PROGRAMMING 

a=[]
for i in range(10):
  num=int(input())
  a.append(num)
print(a)
# NEXT PROGRAMMING 


sum=int(input("Enter the num: "))

for i in range(1,sum):
  print(i*i*i)


sum=int(input("Enter the num: "))
# NEXT PROGRAMMING 
for i in range(1,sum):
  print("Number is ",i,"and cube of the ",i,"is:",i*i*i)

# NEXT PROGRAMMING 
for i in range(1,3):
  print("Week:",i)
  for j in range (1,4):
    print("Day :",j)

# NEXT PROGRAMMING 
for i in range(1,6):
  
  for j in range(0,i):
    print("*",end=" ")
  print()

# NEXT PROGRAMMING 
i=10
while(i>=1):
  print(i)
  i=i-1
