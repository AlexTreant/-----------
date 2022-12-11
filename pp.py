def compare(word1, word2, register=True, spaces=True):
    if register == False:
        word1 = word1.upper()
        word2 = word2.upper()
    if spaces == False:
        word1 = word1.strip()
        word2 = word2.strip()
    print(word1 == word2)


s1 = '  Treant   '
s2 = 'treant'
compare(s1, s2)
compare(s1, s2, register=False)
compare(s1, s2, spaces=False)
compare(s1, s2, register=False, spaces=False)