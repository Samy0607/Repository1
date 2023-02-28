import random
# # ex 1
# a = input("Scrie ce doresti: ")
# assert a[0].upper() == a[-1].upper()

# ex 2.
# stringul = "0123456789"
# print(stringul[::2])
# print(stringul[1::2])

# exercitii optionale
# ex1.
# x = 2345
# if len(str(x)) >= 4:
#     print("e egala cu 4 sau mai mare")
# else:
#     print("are mai putin")

# ex.2
# if len(str(x)) == 6:
#     print("x are exact 6")

# ex3.
# if x % 2 == 0:
#     print("x este par")
# else:
#     print("x este impar")

# ex 4.
# x, y, z = 2, 3, 4
# if x > y and x > z:
#     print("x cel mare")
# elif y > x and y > z:
#     print("y cel mai mare")
# elif z > x and z > y:
#     print("z cel mai mare")
# print(min(x, y, z))

#  ex 5.
# x, y, z = 25, 40, 70
# if x + y + z == 180 and x != 0 and y != 0 and z != 0:
#     print("este triunghi")
# else:
#     print("nu este triunghi")

# ex 6.
# stringul = "Coral is either the stupidest animal or the smartest rock"
# a = int(input("scrie un numar: "))
# print(stringul[:-a])

# ex 7.
# stringul = "Coral is either the stupidest animal or the smartest rock"
# stringul2 = f"{stringul[:5]}{stringul[-5:]}"
# print(stringul2)

# ex 8.
# stringul = "Coral is either the stupidest animal or the smartest rock"
# rock_index = stringul.index("rock")
# print(stringul[:rock_index-1]) # cu -1 scoate spatiul dupa smartest;

# exercitiu bonus
dice_roll = random.randint(1,6)
print(dice_roll)
ghicit = int(input("ghiceste un numar: "))
if dice_roll == ghicit:
    print("numere sunt egale")
elif dice_roll > ghicit:
    print(f"ai ales un numar mai mic, ai ales {ghicit} si era {dice_roll}")
else:
    print(f"ai ales un numar mai mare, ai ales {ghicit} si era {dice_roll}")
