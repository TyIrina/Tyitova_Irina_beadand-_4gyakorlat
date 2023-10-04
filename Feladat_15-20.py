import math

#15. Feladat
#Generáljunk 10 véletlen egész számot, az alábbi intervallumokból:
#[0,10]
#[0,25]
#[0,50]
#[10,75]
#[-50,50]
#[-100,-70]

import random

intervals = [(0, 10), (0, 25), (0, 50), (10, 75), (-50, 50), (-100, -70)]

for _ in range(10):
    interval = random.choice(intervals)
    random_number = random.randint(interval[0], interval[1])
    print(random_number)

#16. Feladat
#Készítsünk programot, amely beolvas egy egész számot, majd kiír a képernyőre egymás mellé ennyi darab * (csillag) karaktert. Módosítsunk most a fenti programon úgy, hogy ne csak egy sornyi csillagot írjon ki, hanem a csillagok segítségével rajzoljon ki egy négyzetet

n = int(input("Adjon meg egy egész számot: "))

if n >= 0:
    csillag= '*' * n
    print(csillag)
else:
    print("A megadott szám negatív")

#Módósíott program:

n= int(input("Adjon meg egy egész számot: "))

if n >= 0:
    for i in range(n):
        print('*' * n)
else:
    print("A megadott szám negatív.")


#17. Feladat
#Kérjünk be két természetes számot (M,N), majd rajzoljunk ki a képernyőre egy MxN méretű téglalapot csillag (*) jelekből.

M = int(input("Adja meg egy számot: "))
N = int(input("Adja meg még egy számot: "))

if M > 0 and N > 0:
    for i in range(M):
        print('*' * N)
else:
    print("M és N-nek pozitívnak kell lenniük.")

#18. Feladat
#Kérjünk be két természetes számot (M,N), majd rajzoljunk ki a képernyőre egy MxN méretű paralelogrammát csillag (*) jelekből (a paralelogrammának N sora legyen, mindegyik sorban M csillaggal).


M = int(input("Adja meg egy számot: "))
N = int(input("Adja meg még egy számot: "))

if M > 0 and N > 0:
    for i in range(N):
        print(' ' * i + '*' * M)
else:
    print("M és N-nek pozitívnak kell lennie..")

#19. Feladat
#Kérjünk be egy természetes számot (N), majd rajzoljunk ki a képernyőre egy háromszöget csillagokból (*). A háromszög N sornyi csillagból álljon.

N = int(input("Adja meg egy számot: "))

if N > 0:
    for i in range(1, N + 1):
        print('*' * i)
else:
    print("N-nek pozitívnak kell lennie.")

#20. Feladat
#Kérjünk be két természetes számot (M,N), majd rajzoljunk ki a képernyőre egy MxN méretű téglalapot csillag (*) jelekből úgy, hogy a téglalap belseje üres legyen.

M = int(input("Adja meg egy számot: "))
N = int(input("Adja meg még egy számot: "))

if M > 0 and N > 0:
    for i in range(M):
        if i == 0 or i == M - 1:
            print('*' * N)
        else:
            print('*' + ' ' * (N - 2) + '*')
else:
    print("M és N-nek pozitívnak kell lennie.")