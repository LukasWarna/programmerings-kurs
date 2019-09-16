points = 0

svar_1 = input('kan grisar flyga?')
if svar_1 == 'nej':
    points = points + 1
else:
    points = points - 1

svar_2 = input('är Jacke sämst?')
if svar_2 == 'ja':
    points = points + 1
else:
    points = points - 1

svar_3 = input('kan jacke flyga?')
if svar_3 == 'nej':
    points = points + 1
else:
    points = points - 1

svar_4 = input('är jacke då en gris?')
if svar_4 == 'ja':
    points = points + 1
else:
    points = points - 1

    print("du fick" + str(points) + " poäng! bra jobbat")

