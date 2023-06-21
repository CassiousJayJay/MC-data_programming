#from add import add
from calculation import add, sub, mul, div

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

