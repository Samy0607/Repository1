# types of params
#########################################################################################################

def plus(a, b):  # a si b sunt parametri (numele folosite pentru argumentele unei functii)
    return a + b


plus(1, 2)  # 1 si 2 sunt argumente (argumentele sunt valorile parametrilor)


#########################################################################################################

# default arguments
def plus(a, b=2):
    return a + b


plus(1)  # daca nu specificam o valoare explicita pentru b atunci va lua valoarea implicita 2
plus(1, 3)


#########################################################################################################

# keyword arguments
def plus_keyword(a, b):
    return a + b


plus_keyword(a=1, b=2)
plus_keyword(b=2, a=1)  # specificand argumentele prin nume nu mai este necesar sa pastram ordinea lor


#########################################################################################################

# variable number of arguments
def plus_many(*args):
    print(args)
    return sum(args)


plus_many(1, 2, 3)
plus_many(2, 4, 6, 8)
plus_many(*[2, 4, 6, 8])  # steluta se mai numeste unpacking.  Linia curenta este echivalenta cu cea anterioara, ca rezultat


def plus_many_2(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


plus_many_2(a=1, b=2)
plus_many_2(a=1, b=2, c=3)
plus_many_2(**{"a": 1, "b": 2, "c": 3})


def plus_many_3(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus_many_3(1, 2, 3, a=6, b=20)
plus_many_3(1, 2)
plus_many_3(a=1, s=5)
plus_many_3()
plus_many_3(a=5)

#def plus_many_4(**kwargs,*args):

# *args, **kwargs este o combinatie specifica pentru functiile care pot sa primeasca  orice fel de argumente