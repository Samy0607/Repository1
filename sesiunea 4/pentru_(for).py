# for i in range(10):
#     print(i)
#
# print(20 * "-", "****", 20 * "-")
#
# for i in range(1, 6):
#     print(i)
#
# print(20 * "-", "****", 20 * "-")
#
# for i in range(1, 6, 2):  # sare cate doua elemente
#     print(i)
#
# print(20 * "-", "iterare folosind Range", 20 * "-")
#
# l = [1, 2, 3, 4, 5]
# for i in range(len(l)):
#     print(f"element: {l[i]}")
#
# print(20 * "-", "For Each", 20 * "-")
#
fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)
# for x in "ana are mere":
#     print(x)
#
# print(20 * "-", "****", 20 * "-")
#
# dct = {
#     "a": 1,
#     "b": 2
# }
# for x in dct:  # iterarea prin dictionar se face prin cheile sale
#     print(x)
#
# for key, value in dct.items():
#     print(key, value)
#
# print(20 * "-", "break in for", 20 * "-")
#
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
#
# print(20 * "-", "continue", 20 * "-")
#
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)
#
# print(20 * "-", "else", 20 * "-")
#
# for x in range(6):
#     print(x)
# else:
#     print("in blocul else")
#
# print(20 * "-", "else + break", 20 * "-")
#
# for x in range(6):
#     print(x)
#     if x == 3:
#         break
# else:
#     print("in blocul else")
#
# print(20 * "-", "nested for", 20 * "-")
#
# adj = ["red", "big", "tasty"]
# for x in adj:
#     for y in fruits:
#         print(x, y)
#
# print(20 * "-", "pass", 20 * "-")
#
# for x in [1, 2, 3]:
#     pass
#     ... # echivalent pentru pass
#
# print(20 * "-", "enumerate", 20 * "-")
#
# for index, elem in enumerate(fruits):  # iterare in acelasi timp prin index si element
#     print(index, elem)