def compare(word1, word2, register=True, spaces=True):
    if register == False and spaces == False:
        return word1.upper().strip() == word2.upper().strip()
    elif register == True and spaces == False:
        return word1.strip() == word2.strip()
    elif register == False and spaces == True:
        return word1.upper() == word2.upper()
    else:
        return word1 == word2


s1 = '  Treant   '
s2 = 'treant'
compare(s1, s2)
compare(s1, s2, register=False)
compare(s1, s2, spaces=False)
compare(s1, s2, register=False, spaces=False)