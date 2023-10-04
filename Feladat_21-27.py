import math

#21. Feladat
#Írj programot az összeadás és a kivonás gyakoroltatására. A program billentyűzetről olvassa be, hogy hány feladatot kell megoldani. Egy feladat a következőkből áll:
#a program generáljon két véletlen számot 1 és 100 között
#olvassa be billentyűzetről a két szám összegét és különbségét.
# a program ellenőrizze le, hogy valóban ez e két szám összege és különbsége.
#minden feladat végén írja ki a képernyőre, hogy jók vagy rosszak az eredmények.
#A program a feladatok végeztével adja meg a helyes és helytelen válaszok arányát.

# *Az adott feladatott sajnos nem tudtam megoldani :c


#22. Feladat
#Írj programot, amely megjeleníti a karakterek kódtáblázatát! Elegendő a 32-255 kódtartományba eső karaktereket megjeleníteni a következő formában:
#Kód Karakter
#32
#33 !
#34 "

print("Kód ")
for code in range(32, 256):
    print(f"{code:3}  {chr(code)}")


#23. Feladat
#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit!

n = int(input("Adjon meg egy pozitív egész számot: "))

if n <= 0:
    print("A számnak pozitívnak kell lennie.")
else:
    print(f"{n} osztói:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

#24. Feladat
#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét!

n = int(input("Adjon meg egy pozitív egész számot: "))

if n <= 0:
    print("A számnak pozitívnak kell lennie.")
else:
    divisors_sum = sum(i for i in range(1, n + 1) if n % i == 0)
    print(f"{n} osztóinak összege: {divisors_sum}")

#25. Feladat
#Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)

n = int(input("Adjon meg egy pozitív egész számot: "))

if n <= 0:
    print("A számnak pozitívnak kell lennie!")
else:
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    if divisors_sum == n:
        print(f"{n} Tökéletes szám.")
    else:
        print(f"{n} Nem tökéletes szám.")

#26. Feladat
#Írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!

alap = float(input("Adja meg a hatványt: "))
kitevő = int(input("Adja meg a kitevőt: "))

hátvány = alap ** kitevő

print(f"{alap}^{kitevő} = {hátvány}")

#27. Feladat
#Írj programot, mely kiírja a Vigenère-táblát! Az első sor az angol ABC betűit tartalmazza, majd minden további sorban az ABC az előző sorhoz képest egyel eltolva szerepel.
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE


abc= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    shifted_alphabet = alphabet[i:] + alphabet[:i]
    print(shifted_alphabet)