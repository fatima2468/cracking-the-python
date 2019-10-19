import string

# Exercise-2: Check if the string has balanced paranthesis
# Time Complexity: O(N) - Space Complexity: Half the size of length of String (N/2)
def check_balanced_parenthesis(test_case: string):
    balanced = True
    paran_stack = []
    start_paran = ["[", "{", "("]
    paran = { "]":"[", "}":"{", ")":"(" }

    for i in range(0, len(test_case)):
        val = test_case[i]
        if val in start_paran:
            paran_stack.append(val)
        else:
            popped_val = paran_stack.pop()
            if popped_val != paran.get(val):
                balanced = False
                break

    if len(paran_stack):
        balanced = False

    return balanced


test_case1 = "{[(])}"
test_case2 = "{([])}"
test_case3 = "[()]{}{[()()]()}"
test_case4 = "[(])"
test_case5 = "{()}[]["

print(f""" check_balanced_parenthesis(test_case1="{[(])}") : {check_balanced_parenthesis(test_case1)}""")
print(f""" check_balanced_parenthesis(test_case2 = "{([])}") : {check_balanced_parenthesis(test_case2)}""")
print(""" check_balanced_parenthesis(test_case3 = "[()]{}{[()()]()}}" : """ + check_balanced_parenthesis(test_case3))
print(""" check_balanced_parenthesis(test_case4 = "[[(])" : """ + check_balanced_parenthesis(test_case4))
print(f""" check_balanced_parenthesis(test_case5 = "{()}[][") : {check_balanced_parenthesis(test_case5)}""")

print(check_balanced_parenthesis(test_case2))
print(check_balanced_parenthesis(test_case3))
#print(check_balanced_parenthesis(test_case4))
print(check_balanced_parenthesis(test_case5))
