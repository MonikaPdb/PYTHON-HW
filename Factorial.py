def faktorial(cislo): 
    while True: 
        try:
            cislo=int(input('Vloz cele cislo, funkce vypise jeho faktorial. Cislo : '))
            if True:
                 vysledek = 1
                 while cislo < 0:
                     print('Nevlozil/a jsi kladne cislo.')
                     cislo=int(input('Vloz cele cislo, funkce vypise jeho faktorial. Cislo : '))            
                 while cislo >= 1:
                     vysledek = vysledek * cislo
                     cislo = cislo - 1
                 print('Faktorial je', vysledek)
                 break
        except ValueError:
            print('Nevlozil/a jsi cele cislo.')
            pass
   
faktorial(cislo)
