

klass = {
    'lisa': 8, 
    'kalle': 7,
    'pelle': 6
    }

summa = 0

for elev in klass:
    print (elev)
    summa = summa + klass[elev]
print (summa/len(klass))

for elev in sorted(klass, key=klass.get):
    print(elev)
