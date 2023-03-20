# # 1. if
# a = 33
# b = 200
# if a < b :
#     print("a < b")
#
# if b:
#     print("b nu este False")
#
# if a == 0 :
#     print("a este 0") # nu se executa linia de cod pt ca linia este falsa
#
# if b and b > a :
#     print("test")

# # 2. if...else
# a = 333
# b = 200
# if b > a :
#     print("b este mai mare")
# else:
#     print("a este mai mare")
#
# # 3. if...elif...else
# a = 333
# b = 0
# if b > a:
#     print("b este mai mare")
# elif b == a:
#     print("b este egal cu a")
# elif b == 0:
#     print("b este 0")
# else: # nu e obligatoriu sa avem else aici
#     print("b nu este mai mare decat a")

# 4. Shorthand
a = 333
b = 200
x = a if a > b else b
print(a) if a > b else print(b)
print(x)