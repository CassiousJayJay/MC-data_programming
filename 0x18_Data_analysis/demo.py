def main():
    a = 40
    b = 60
    print(sum(a, b))

    add = lambda x, y: x + y
    c = add(a, b)
    print(c)

    hello = lambda n: print("Hello, World {}".format(n))
    hello("James")
    print(1, 2, 3, 4, 5, 6, 7)
    print_all_2(1, 2, 3, 4, 56, 78, 90)
    fake_infor(key="name", value="James")

def sum(x:int, y:int):
    return x + y

def print_all(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)

def print_all_2(*args):
    print(type (args))
    sum = 0
    for i in args:
        sum +=i
        print(sum)

def fake_infor(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(f"${i}")

   


if __name__=="__main__":
    main()