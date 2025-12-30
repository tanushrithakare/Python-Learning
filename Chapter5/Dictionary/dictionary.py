Student={"Tanu":1,"Akash":2,"Riya":3}
print(type(Student))
print(dict.keys(Student))
print(dict.values(Student))
print(Student["Tanu"])
#dictionary are mutable,unordered and dont allow duplicate keys  
Student["Tanu"]=2
print(dict.values(Student))
Student.pop("Tanu")
print(Student)
print(Student.items())
print(type(Student))
