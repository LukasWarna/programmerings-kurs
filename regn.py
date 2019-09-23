points = 0

def kontrollera_svar(ratt_svar, anvandarens_svar):
    if anvandarens_svar == ratt_svar:
        points = points +1
    else:
        points = points -1

svar_1 = input('kan grisar flyga?')
kontrollera_svar('nej', svar_1)

svar_2 = input('är Jacke sämst?')
kontrollera_svar('ja', svar_2)

svar_3 = input('kan jacke flyga?')
kontrollera_svar('nej', svar_3)

svar_4 = input('är jacke då en gris?')
kontrollera_svar('ja', svar_4)

print("du fick" + str( points) + " poäng! bra jobbat")

