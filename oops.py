class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(self.salary)

Paras = Employee("Paras","1,10,00000")
# print(Paras.name)
# print(Paras.salary)
Paras.getSalary()

karan = Employee("Karan","5,10,00000")
# print(karan.name)
# print(karan.salary)
karan.getSalary()