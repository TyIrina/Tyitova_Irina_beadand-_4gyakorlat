import math

#3. Feladat
#Kérjünk be két egész számot! Írjuk ki a számokat az első számtól a másodikig! Figyeljünk arra, hogy nem biztos, hogy az első szám a kisebb! Kérjünk be a lépésközt is!

szam1 = int(input("kérem az első számot: "))
szam2 = int(input("kérem a második számot: "))
lepeskoz = int(input("léptetés: "))

if szam1 < szam2:
    for i in range(szam1,szam2, lepeskoz):
        print(i)
elif szam2 < szam1:
    for i in range(szam2,szam1,lepeskoz):
        print(i)
else:
    print("A két szám egyenlő:")

#4. Feladat
#Írjuk ki az első n db négyzetszámot, egymás mellé, pontosvesszővel elválasztva!

szám = int(input("Hány négyzetszámot szeretne kiírni: "))

sorozat = [i**2 for i in range(1, szám+1)]
print(*sorozat, sep="; ")

#5. Feladat
#Írjuk ki az első n db köbszámot, egymás alá!

szám = int(input("Hány négyzetszámot szeretne: "))

sorozat = [i**2 for i in range(1, szám+1)]
print(*sorozat, sep="; ")

#6. Feladat
#Írjuk ki egy megadott a és b egész érték közötti egész számok négyzetgyökeit, 2 tizedes jegy pontossággal!

a = int(input("'a' egész szám: "))
b = int(input("'b' egész szám: "))

for i in range(a, b + 1):
    if i >= 0:
        sqrt_i = math.sqrt(i)
        print(f"A(z) {i}-nek a négyzetgyöke: {sqrt_i:.2f}")


#7. Feladat
#Készítsünk faktoriálist számító programot, amely kiszámolja n faktoriálist. pl.: 3!=3*2*1=6

a = int(input("Adjon meg egy számot: "))

if a < 0:
    print("A faktoriális csak pozitív szám lehet.")
elif a == 0:
    print("0 faktoriálisa 1.")
else:
    faktorial = 1
    for i in range(1, a + 1):
        faktorial *= i
    print(f"{a}! = {faktorial}")


#8. Feladat
#Készíts programot, amely kiírja az első N négyzetszámot.

a = int(input("Hány négyzetszámot szeretne: "))

for i in range(1, a + 1):
    square = i ** 2
    print(square)


#9. Feladat
#Készíts programot, amely kiírja az N-nél nem nagyobb páratlan számok összegét.

n = int(input("Adja meg az N szám értékét: "))

összeg = 0

for szam in range(1, n + 1, 2):
    összeg += szam

print(f"Az N-nél nem nagyobb páratlan számok összege: {összeg}")


#10. Feladat
#Készíts programot, amely bekéri a K pozitív egész számot, majd kiszámolja a következő összeget: 1·2 + 2·3 + 3·4 + 4·5 + ... + K·(K+1)

K = int(input("Adja meg K pozitív egész számot: "))

összeg = 0

for i in range(1, K + 1):
    összeg += i * (i + 1)

print(f"Számok összege: {összeg}")


#11. Feladat
#Kérjünk be egy N természetes számot, majd írassuk ki a három összes olyan többszörösét, amely kisebb vagy egyenlő mint N.

N = int(input("Adjon meg egy természetes számot: "))

print(f"{N} számnáé kisebb vagy egyenlő háromszoros számok:")

for i in range(0, N + 1, 3):
    print(i)


#12. Feladat
#Program, amely kiírja az első N Fibonacci számot. Fibonacci-számok: Az első két elem 0 és 1, a további elemeket az előző kettő összegeként kapjuk.
#Képletben: Ha F0=0 és F1=1 akkor a következő elemeket úgy kapjuk, hogy Fn=Fn-1+Fn-2
#Az első néhány Fibonacci-szám: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

N = int(input("Hány Fibonacci számot szeretne kiírni: "))

elsőelem = [0, 1] 

while len(elsőelem) < N:
    next_fib = elsőelem[-1] + elsőelem[-2] 
    elsőelem.append(next_fib)

print(f"Az első {N} Fibonacci szám:")
for num in elsőelem:
    print(num, end=" ")


#13. Feladat
#Program, amely kiírja az első N prímszámot. Prímszámok a csak az 1-el és önmagával osztható számok.

N = int(input("Hány prímszámot szeretne: "))

prím = []
szám = 2

while len(prím) < N:
    is_prime = True
    for i in range(2, int(szám ** 0.5)):
        if szám % i == 0:
            is_prime = False
            break
    if is_prime:
        prím.append(szám)
    szám += 1

print(f"Az első {N} prímszám:")
for prime in prím:
    print(prime, end=" ")


#14. Feladat
#Írj programot, amely megjelenít egy szorzótáblát így, vagy ennél szebben:
#* 1 2 3
#-------
#1 ¦ 1 2 3
#2 ¦ 2 4 6
#3 ¦ 3 6 9


n = int(input("Milyen szorzótáblát szeretne: "))

print("*", end=" ")
for i in range(1, n + 1):
    print(i, end=" ")
print("\n" + "-" * (n * 2 + 3))

for i in range(1, n + 1):
    print(f"{i} ¦", end=" ")
    for j in range(1, n + 1):
        result = i * j
        print(result, end=" ")
    print()










