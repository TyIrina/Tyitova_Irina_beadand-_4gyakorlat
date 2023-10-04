#Írjunk ki a képernyőre 100 db csillagot!
for i in range(100):
    print("*", end="")

#Írjunk ki a képernyőre 5 darabszámú, $ karaktert!

for i in range(5):
    print("$", end="")


# Kérjünk be egy szöveget, majd keretezzük körbe csillagokkal!

bekertSzoveg = input("Kérem a bekeretezendő szöveget: ")
keret = ""
for i in range(len(bekertSzoveg) + 4):
    keret += "*"
print(keret)
print(f"* {bekertSzoveg} *")
print(keret)


#Rajzoljunk le egy 8*8-as sakktáblát csillagokból és szóközökből!

paros=" * * * *"
paratlan="* * * * "
for i in range(8):
    if i%2==0:
        print(paros)
    else:
        print(paratlan)