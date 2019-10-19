import string

#Exercise-1: Implement an algorithm to determine if a string has all unique characters

# Solution 1 (No Additinal DataStructure)
# Solution-1: Time Complexity: O(N^2)
def isUniqueCharSeq(input:string):
    # No Additional DataStructure Used
    if len(input) > 128:
       return False

    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            # print(f"{ord(input[i])} -- {ord(input[j])}")
            if input[i] == input[j]:
                return False
    return True




# Solution-2 (using Additinal DataStructure)
# Solution-2: Time Complexity: O(N) with additional space equivalent to the characterset
def isUniqueCharSequence(input:string):
    # Assuming the string is an ASCII 128 character set
    if len(input) > 128:
        return False

    charSet = [False]*128

    for i in range(0, len(input)):
        val = ord(input[i])
        # print(f"{input[i]} -- {ord(input[i])}  -- {val}")

        if charSet[val]:
            return False

        charSet[val] = True
    return True

print (f"""TestCase1: String "isjkdhks" holds unique charcaters:  {isUniqueCharSeq("isjkdhks")}""")
print (f"""TestCase2: String "abc%defgh!" holds unique charcaters:  {isUniqueCharSeq("abc%defgh!")}""")
print()
print (f"""TestCase1 : String "isjkdhks" holds unique charcaters:  {isUniqueCharSequence("isjkdhks")}""")
print (f"""TestCase2: String "abc%defgh!" holds unique charcaters:  {isUniqueCharSequence("abc%defgh!")}""")
