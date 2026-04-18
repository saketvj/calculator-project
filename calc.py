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

# function to convert input expression to tokens. we need to handle multi digit and decimal numbers and handle operators and parentheses as well. 

def flush_number( lst, number):
    
    if number:
        lst.append(float(number))
        number = ''
    return number
    
def tokeniser(expression):
    number = ''
    tokens = []
    for char in expression:
        if char in precedence or char in '()':
            number = flush_number( tokens, number)
            tokens.append(char)
        else:
            number +=char
    number = flush_number(tokens, number)
    return tokens


def convert_to_rpn(tokens):
    st = []
    output = []

    for token in tokens:
        if token in precedence:
            while len(st) > 0 and st[-1] != '(' and precedence[st[-1]] >= precedence[token]:
                
                output.append(('Operator', st[-1]))
                st.pop()
            st.append(token)
        
        elif token == '(':
            st.append(token)

        elif token == ')':
            
            while st[-1] != '(':
                output.append(('Operator', st[-1]))
                st.pop()
            st.pop()
        else:
            output.append(('Operand', token))
# print(number)
# output.append(number)
    while len(st) > 0:
        output.append(('Operator', st[-1]))
        st.pop()
    
    return output


# # some edge cases to consider:
# # 1. negative numbers.
# # 2. multplication when no multiplication sign is given. eg 2(3+4) should be treated as 2*(3+4).
# # 3. multiple operators in a row. eg 2++3 should be treated as 2+3.
# # 4. exponentiation operator. eg 2^3 should be treated as 2**3.

# # now we have the output in the form of RPN. we need to evaluate it now.

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
        


def evaluator(output):
    temp = []
    for token_type,value in output:
        
        if token_type == 'Operator':
            if len(temp) < 2:
                raise ValueError("Invalid expression")
            b = temp.pop()
            a = temp.pop()
            # print(a,b)
            ans = solve(a,b,value)
            temp.append(ans)
        else:
            temp.append(value)
    result = temp.pop()
    return result



# print(tokeniser(expression))
# print(convert_ti_rpn(tokeniser(expression)))
print(evaluator(convert_to_rpn(tokeniser(expression))))
# print(result)