    
def mycapitalize():
    import re
    print('The function will capitalize the first character in every word in a given sentence.')
    sentence = input('Insert a sentence. Sentence can only contain characters a-z and space and cannot be blank or only spaces. Insert your sentence: ')
    result = ''
    while not re.match("^[a-z ]*$", sentence) or (not sentence or sentence.isspace()):
        sentence = input('Your input was not valid. Try again: ')
    if re.match("^[a-z ]*$", sentence): 
        splitting = sentence.split()
        cap = [word[0].upper() + word[1:] for word in splitting]
        result = ' '.join(cap)
        print('Your input was valid. Here is the sentence:', result)
        
mycapitalize()
