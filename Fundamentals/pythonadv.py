a=10

def f1():
    a=222
    print(a)
    print(globals()['a'])

def f2():
    print(a)

f1()
f2()

