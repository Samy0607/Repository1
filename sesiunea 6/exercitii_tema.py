# 1.
class Cerc:
    raza = 5
    culoare = "Maro"

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
        return (3.14 * (self.raza ** 2))

    def diametru(self):
        return (self.raza * 2)

    def circumferinta(self):
        return (2 * (self.diametru()))


c = Cerc(5, "Maro")
c.descriere_cerc()
print(c.aria())
print(c.diametru())
print(c.circumferinta())


# 2.
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}")
    def aria(self):
        return (self.lungime * self.latime)

    def perimetrul(self):
        return (2 * (self.latime * self.lungime))

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



d = Dreptunghi(2, 4, "gri")
d.descriere()
print(d.aria())
print(d.perimetrul())
d.schimba_culoarea("verde")
d.descriere()

# 3.
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f"Domnul {self.nume} {self.prenume} lucreaza ca distribuitor pentru un salariu de {self.salariu} lei pe luna")

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return (12 * self.salariu)

    def marire_salariu(self, procent):
        self.salariu += self.salariu * (procent / 100)

a = Angajat("Alexa", "Sorin", 2000)
a.descriere()
print(a.nume_complet())
print(a.salariu_lunar())
print(a.salariu_anual())
a.marire_salariu(25)
print(a.salariu_lunar())
print(a.descriere())

# 4.
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma

c = Cont(123456, "Potop_Samuel", 5000)
c.afisare_sold()
c.debitare_cont(200)
print(c.afisare_sold())
c.creditare_cont(700)
print(c.afisare_sold())