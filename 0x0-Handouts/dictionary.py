student = {"name": "James", "age": 45, "courses": ["maths", "linux", "computer science"]}

#deleting
#age = student.pop("age") 
#del student["age"]

#updating
#student["phone"] = "+260972983537" #update
# student.update({"name": "Jane", "age": 56, "phone": +260972983537})

print(student.get("phone", "Not found"))
for key in student:
    print(key)
print(len(student))
print(student.keys())
print(student.items())
print(student.values())
print(student)