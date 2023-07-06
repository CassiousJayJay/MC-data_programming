
#squares = [i * i for i in range(11)]
#print(squares)

names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
new_names = []

for i in names:
    if 'a' in i:
        new_names.append(i)
print(new_names)

names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
new_names = [i for i in names if 'a' in i]
print(new_names)

#sort in alphabetically
names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
new_names.sort()
print(new_names)

#sort in reverse order
names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
new_names.sort(reverse= True)
print(new_names)

#copy a list
names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
new_names = names.copy()
print(new_names)

#joining and sorting a list
names = ["James", "Andrew", "John", "Cassious", "Mathews", "Brighton"]
names_2 = ["cat", "Dog", "Lion", "elephants"]
total_names = names + names_2
total_names.sort()
total_names.count(total_names)
print(total_names)