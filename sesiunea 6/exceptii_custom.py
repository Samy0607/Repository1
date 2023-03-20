class CustomException(Exception):
    pass


# Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative.
# Daca da sa se arunce o exceptie specifica.
class ContainsNegativeNumberException(Exception):
    pass


def verify_negativ_number(numbers):
    for n in numbers:
        if n < 0:
            raise ContainsNegativeNumberException(f"Il contine pe {n}")


verify_negativ_number([1, 3, 5, -3, -4])
