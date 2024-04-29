class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @property
    def fullname(self):
        return f"{self.name} {self.lastname}"

    @fullname.setter
    def fullname(self, first_last):
        self.name, self.lastname = first_last.split()

    @fullname.deleter
    def fullname(self):
        self.lastname = None
        print('Dane usunięte!')


anna = Person('Anna', 'Kowalaska', 30)
print(anna.fullname)

anna.fullname = 'Anna Nowak'
print(anna.name, anna.lastname)

del anna.fullname
print(anna.name, anna.lastname)
