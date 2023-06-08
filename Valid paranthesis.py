# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Sample Input 1 :

# 2
# [()]{}{[()()]()}
# [(])

# Sample Output 1 :
# Balanced
# Not Balanced

# Explanation Of The Sample Input 1 :
# In TestCase 1 there is always an opening brace before a closing brace i.e ‘{‘ before ‘}’, ‘(‘ before ‘)’, ‘[‘ before ‘]’.

# In TestCase 2 there is closing brace for ‘[‘ i.e. ‘]’ before closing brace for ‘(‘ i.e. ‘)’. The balanced sequence should be ‘[()]’.

# Sample Input 2 :
# 2
# [[}[
# []{}()

# Sample Output 2 :
# Not Balanced
# Balanced

# SOLUTION:

def isValidParenthesis(expression):

    # Write your code here.
    res = []
    for i in expression:
        if i == '{' or i == '[' or i == '(':
            res.append(i)
        else:
            if len(res):
                if res[-1] == '(' and i == ')':
                    res.pop()
                elif res[-1] == '{' and i == '}':
                    res.pop()
                elif res[-1] == '[' and i == ']':
                    res.pop()
                else:
                    return False
            else: 
                return False
    
    if (len(res)):
        return False
    return True

# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
