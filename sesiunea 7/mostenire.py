class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")


class Student(Person):
    pass


class Worker(Person):
    def __init__(self, age, name, job):
        # Person.__init__(self, age, name)
        super().__init__(age, name)
        self.job = job


p = Person(18, "Mike")
p.print_name()

st = Student(20, "John")
st.print_name()

wk1 = Worker(21, "Leti", "Bancher")
wk1.print_name()
print(wk1.job)
print(wk1.age)

print(type(p))
print(type(st))
print(type(wk1))
