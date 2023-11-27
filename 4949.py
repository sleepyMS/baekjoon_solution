import sys
input = sys.stdin.readline


while True:
    result = 'yes'
    stack = []
    tmp = input().rstrip()
    if tmp == '.':
        break
    
    for s in tmp:
        if s == '(':
            stack.append(')')
        if s == '[':
            stack.append(']')
        if s == ')':
            if not len(stack):
                result = 'no'
                break
            if not (s == stack.pop()):
                result = 'no'
                break
        if s == ']':
            if not len(stack):
                result = 'no'
                break
            if not (s == stack.pop()):
                result = 'no'
                break

    if len(stack):
        result = 'no'
        
    print(result)