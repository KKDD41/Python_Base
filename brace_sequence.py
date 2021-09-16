import math, sys
import stack_list as st

# способ получения корректного скобочного выражения:
# '' - норм
# A = [B], A = (B) -- норм 
# C = AB -- норм
# тут correct вычисляет, является ли данное скобочное выражение корректным 

S = input()
_stack = []

def reverse(x, y):
    return (( x=='(' and y==')' ) or ( x=='[' and y==']' ))

def correct(S: str):
    for b in S:
        if b == '(' or b == '[':
            st.push(_stack, b)
        else:
            if st.size(_stack) == 0:
                return False
            else:
                a = st.top(_stack)
                if reverse(a, b):
                    _stack.pop()
                else:
                    return False
    return False if st.size(_stack)>0 else True
    
print(correct(S))