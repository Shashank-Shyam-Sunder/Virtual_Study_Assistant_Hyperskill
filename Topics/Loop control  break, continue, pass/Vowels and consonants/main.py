word =  input()
vowels = 'aeiou'

for i in word:
    if i.isalpha() == True:
        if i in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break



