# 1. Írjunk ki a képernyőre 0-tól 50-ig a számokat egymás alá.
for i in range(51):
    print(i)

# 2. Írjuk ki a számokat egymás alá 182-től 212-ig.
for i in range(182, 212+1):
    print(i)

# 3. Írjuk ki a páros számokat egymás alá 100-től 200-ig.
for i in range(100, 200+1, 2):
    print(i)

# 4. Írjuk ki a páratlan számokat egymás alá 89-től 57-ig visszafelé.
for i in range(89, 57-1, -2):
    print(i)

# 5.  Írassuk ki 1-től 20-ig a számokat és négyzetüket!
for i in range(1,20+1):
    print(i, i*i)

# 6. Írassuk ki 99-től csökkenő sorrendben az összes pozitív, 3-mal osztható egész számot!
for i in range(99,0,-3):
    print(i)

# 7. Írassuk ki 101-től 50-ig cskkenő sorrendben az öttel osztható számok kétszeresét!
for i in range(100, 50-1,-5):
    print(i*2)

# 8. Írjuk ki a képernyőre az egész számokat 1-től 1000-ig, vesszővel elválasztva, az utolsó szám után pont legyen!
for i in range(1, 1001):
    if i == 1000:
        print(i, end='.')
    else:
        print(i, end=', ')

# 9. Írjuk ki a képernyőre az egész számokat 1000-től 1-ig, visszafelé 3-asával!

for i in range(1000, 0, -3):
    print(i)