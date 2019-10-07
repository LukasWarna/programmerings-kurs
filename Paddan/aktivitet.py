import random


sol_aktiviteter = ['cykla', 'simma', 'fotboll', 'sola', 'springa']
regn_aktiviteter = ['netflix', 'regndans', 'läsning', 'träna', 'kocka']

prognos = input('Är det det bra eller dåligt väder där ute?')


if prognos == "bra":
    print (random.choice(sol_aktiviteter))
if prognos == "dåligt":
    print(random.choice(sol_aktiviteter))
        



