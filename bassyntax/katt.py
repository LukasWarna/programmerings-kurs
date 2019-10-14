

class Cat:
    def __init__(self, ålder, namn, färg, favoritgodis):
        self.ålder = ålder 
        self.namn = namn 
        self.färg = färg 
        self.favoritgodis = favoritgodis 

    def __repr__(self):
        return self.namn  + self.ålder  + self.färg  + self.favoritgodis 

c1 = Cat("1", "2", "blå", "3")
c2 = Cat("4", "3", "röd", "1")
    
print(c1)
print(c2.namn)

katter = []


open = True

while open:
    val = input("vad vill ni göra?  lägga till (L), stäng (S)").lower()
    if val == 's':
        open = False
    elif val == 'l':
        namn = input("kattens namn")
        ålder = input("Ålder?")
        färg = input("Färg?")
        godis = input("favoritgodis")

        nya_katten = Cat(ålder, namn, färg, godis)

        katter.append(nya_katten)
print(katter)



