import string

# Exercise Palindrome Permutation: Given a string, write a function to check if it is permutation of a palindrome.
def checkpalindrome(input:string):
    isPal = True;
    count_charmap = {};

    for i in range(0, len(input)):
        key = ord(input[i])
        if key in count_charmap:
            count_charmap[key] += 1
        else:
            count_charmap[key] = 1

    found_odd_occur = False
    for key in count_charmap:
        val = count_charmap.get(key)
        if val % 2 != 0:
            if found_odd_occur:
                isPal = False
                break;

            found_odd_occur = True
    return isPal

print()
print (f"""TestCase1 : Check if string is a Palindrom -- checkpalindrome("tceetca"): {checkpalindrome("tceetca")}""")
print (f"""TestCase2 : Check if string is a Palindrom -- checkpalindrome("tcetect"): {checkpalindrome("tcetect")}""")
print (f"""TestCase3 : Check if string is a Palindrom -- checkpalindrome("tcetecta"): {checkpalindrome("tcetecta")}""")
