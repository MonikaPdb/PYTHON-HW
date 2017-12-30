def faktorial(): 
    while True: 
        try:
            cislo=int(input('Vloz cele kladne cislo, funkce vypise jeho faktorial. Cislo: '))
            if True:
                 vysledek = 1
                 while cislo < 0:
                     print('Podarilo se ti zadat cele cislo. Bohuzel ale nebylo kladne. Zkus to znova.')
                     cislo=int(input('Vloz cele cislo, funkce vypise jeho faktorial. Cislo: '))            
                 while cislo >= 1:
                     vysledek = vysledek * cislo
                     cislo = cislo - 1
                 print('Faktorial je', vysledek)
                 break
        except ValueError:
            print('Nevlozil/a jsi cele kladne cislo. Zkus to znova.')
            pass            
    
faktorial()
