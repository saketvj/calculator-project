import sys

# def add( a,  b):
#     return a+b

# def subtract( a,  b):
#     return a-b

# def multiply( a,  b):
#     return a*b  

# def divide( a,  b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a/b        


# expression = sys.argv[1].replace(" ", "")
# if '+' in expression:
#     a, b = map(float, expression.split('+'))
#     print( add(a,b))
# elif '-' in expression:
#     a, b = map(float, expression.split('-'))            
#     print(subtract(a,b))
# elif '*' in expression:
#     a, b = map(float, expression.split('*'))
#     print(multiply(a,b))
# elif '/' in expression:
#     a, b = map(float, expression.split('/'))
#     print(divide(a,b))
    

# RPN (Reverse Polish notation  using shunting algorithm)
import sys
expression = sys.argv[1].replace(" ", "")
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
st = []
output = []
number = ''

for char in expression:
    if char in precedence:
        
        if number:
            output.append(float(number))
        number = ''
        if len(st) > 0 and st[-1] == '(':
            st.append(char) 
        elif len(st) > 0 and precedence[st[-1]] >= precedence[char]: 
            while len(st) > 0 and st[-1] != '(' and precedence[st[-1]] >= precedence[char]:
                output.append(st[-1])
                st.pop()
            st.append(char)
        else:
            st.append(char)
       

    elif char == '(':
        st.append(char)
        if number:
            output.append(float(number))
        number = ''
    elif char == ')':
        if number:
            output.append(float(number))
        number = ''
        while st[-1] != '(':
            output.append(st[-1])
            st.pop()
        st.pop()
        
    else:
        # we need to handle multi digit and decimal numbers here.
        number += char
        # directly pushing the numbers in the output.

# print(number)
if number:
    output.append(float(number))
while len(st) > 0:
    output.append(st[-1])
    st.pop()
# print(output)

# some edge cases to consider:
# 1. negative numbers.
# 2. multplication when no multiplication sign is given. eg 2(3+4) should be treated as 2*(3+4).
# 3. multiple operators in a row. eg 2++3 should be treated as 2+3.
# 4. exponentiation operator. eg 2^3 should be treated as 2**3.

# now we have the output in the form of RPN. we need to evaluate it now.

def solve(a,b,char):
    if char == '+':
        return a+b
    elif char == '-':
        return a-b
    elif char == '*':
        return a*b
    elif char == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a/b
        
temp = []

for char in output:
    if char in precedence:
        b = temp.pop()
        a = temp.pop()
        # print(a,b)
        ans = solve(a,b,char)
        temp.append(ans)
    else:
        temp.append(char)

result = temp.pop()

print(result)