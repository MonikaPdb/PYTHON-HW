def myfactorial(): 
    while True: 
        try:
            number = int(input('Insert whole positive number, the function will return its factorial. Insert number: '))
            if True:
                 result = 1
                 while number < 0:
                     print('You inserted whole negative number. Try again: .')
                     number = int(input('Insert whole positive number, the function will return its factorial. Insert number: '))            
                 while number >= 1:
                     result = result * number
                     number = number - 1
                 print('Factorial is', result)
                 break
        except ValueError:
            print('You have not inserted whole positive number. Try again: ')
            pass            
    
myfactorial()

