numbers = [1, 2, 3, 4, 5, 6]
first = set(numbers)

# print(uniques)
second = {7, 8, 9, 4, 5}

# second.clear()
print(first | second)# union
print(first & second) # intersection
print(first - second) # difference
print(first ^ second) # either in first or second but not in bot sets

if 1 in second:
    print("Yes")
else:
    print("1 is not in the Set")