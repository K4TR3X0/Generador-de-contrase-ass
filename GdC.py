import random
Caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

oa = int(input("¿Cuantos caracteres tendra la contraseña?:"))
C = ""

for i in range(oa):
    letra = random.choice(Caracteres)
    C = C + letra
print(C)
