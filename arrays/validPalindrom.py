def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum())
    s = s.lower()
    print(s)
    stringlist = [x for x in s]
    i = 0
    j = len(stringlist) - 1
    while i < j:
        if stringlist[i] != stringlist[j]:
            return False
        i += 1
        j -= 1
    return True

def isPalindromeEasy(s):
    s = s.replace(" ","")
    s = s.lower()
    return s == s[::-1]

s="Madam, in Eden, I'm Adam"
print(isPalindrome(s))