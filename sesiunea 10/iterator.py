# folosit in cadrul unei clase

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.generated_nrs = 0
        self.nr = 0

    def __iter__(self):
        return self


    def __next__(self):
        self.nr += 1
        if self.generated_nrs >= self.n:
            raise StopIteration
        elif self.nr % 2 == 0:
            self.generated_nrs += 1
            return self.nr
        return self.__next__()


it = EvenIterator(10)
for i in it:
    print(i)

it = EvenIterator(10)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break