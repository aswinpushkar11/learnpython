class Car:
    def __init__(self,name,model,version):
        self.name = name
        self.model = model
        self.version = version
    
    def getcarinfo(self):
        print(f'The specifications of the car are:\n\tCompanyName:{self.name}\n\tModel:{self.model}\n\tVesrsion:{self.version}')


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print(f'{self.name} likes beer-biriyani')


class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car
    def getworkinfo(self):
        print(f'{self.name} is a Python Developer')
    def getinfo(self):
        print('Employee Information:')
        print(f'\tEmployee name :{self.name}\n\tEmployeeAge:{self.age}\n\tEmployeeNo={self.eno}\n\tEmployeeSal={self.esal}')
        print()
        self.car.getcarinfo()

c=Car('Skoda','Slavia','1.5T')
e=Employee('Aswin',29,1224324,'28k',c)
e.eatndrink()
e.getworkinfo()
e.getinfo()
# e.car.getcarinfo()

