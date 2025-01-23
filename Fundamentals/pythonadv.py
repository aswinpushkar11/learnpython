class University:
    def __init__(self):
        print('Outer class object created')

    class Department:
        def __init__(self):
            print('Inner class object created')
        def m1(self):
            print('Calling Inner method')

# u = University()
# d = u.Department()
# d.m1()

# d=University().Department()
# d.m1()

University().Department().m1()