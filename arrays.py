names = []
print(names)
names = ["John", "Sam", "Tony"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print("backword index:")
print(names[-1])
print(names[-2])
print(names[-3])
names.append("Paul")
print(names)

age = [23,45,33,56]
names.extend(age)
print(names)
names.remove("Sam")
print(names)


print(len(names))
print(max(age))
