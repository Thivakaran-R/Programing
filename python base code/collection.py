
#LIST
a=[1,2,3,4,5,6]
print(a)
a.append(7)
print(a)

a=[1,2,3,4,5,6]
b=[7,8]
a.extend(b)
print(a)

a=[1,2,3,4,5,6]
a.append(7)
print(a)

a=[1,2,3,4,5,6]
a.pop(5)
print(a)

a=(1,2,3,4,5,6)
b=list(a)
print(a)
print(b)
b.pop()
print(b)

#TUPLE
a=(1,2,3,4,5,6)
b=list(a)
print(type(b))

#SET
a={1,2,3,4,5,6}
print(a)
a.pop()
print(a)


a={1,2,3,4,5,6}
print(a)
a.add(10)
print(a)


a={1,2,3,4,5,6}
print(a)
a.remove(6)
print(a)

#DICTIONARY
a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
print(a)


a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
print(a.get("name")


a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
print(a.values())



a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
a.update({"age":23})
print(a)


a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
a.pop("age")
print(a)

a={
  "name":"cse",
  "age":21,
  "year":2024,
  "student":{"RAVI","BALA"}
}
a.clear()
print(a)


      