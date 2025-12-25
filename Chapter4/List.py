#List in python
Food=["Gulab Jamun","Jalebi","Samosa"]
print(Food[1])
print(len(Food))
print(max(Food))
print(min(Food))

#indexing
Marks=[100,98,99,75]
print(len(Marks))
Marks[2]=34
print(Marks)

#slicing
print(Marks[1:3])
print(max(Marks))
print(min(Marks))

#insering element
Marks.insert(0,89)
print(Marks)

Marks.append(101)
print(Marks)

Marks.remove(34)
print(Marks)

Marks.pop(3)
print(Marks)

Marks.sort()
print(Marks)

Marks.reverse()
print(Marks)

#Practice question 2
Food1=(input("Enter 1 Fav Food Name:"))
Food2=(input("Enter 2 Fav Food Name:"))
Food3=(input("Enter 3 Fav Food Name:"))
Food_list=[Food1,Food2,Food3]
print("your list is this ",Food_list)

