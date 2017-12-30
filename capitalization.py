def kapitalizace():
    import re
    zadani = input('Napis vetu. Veta muze obsahovat pouze mezery a mala pismena, bez diaktiriky. Tva veta: ')
    vysledek = ''
    while not re.match("^[a-z ]*$", zadani):
        zadani = input('Zadani bylo spatne, zkus to znova. Tva veta: ')
    if re.match("^[a-z ]*$", zadani): 
        rozsekani = zadani.split()
        kapitalizace = [word[0].upper() + word[1:] for word in rozsekani]
        vysledek = ' '.join(kapitalizace)
        print('Vetu si zadal dobre. Zde je vysledek funkce:', vysledek)
kapitalizace()
