def balanced_stack(expre):
    stack = []
    for char in expre:
        if char in '({[':
            stack.append(char)
        elif char in ')':
            ## if we access stack[-1] != '(' then it will return stack is empty
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char in '}':
            if not stack or stack[-1] != '}':
                return False
            stack.pop()
        elif char in ')':
            if not stack or stack[-1] != ']':
                return False
            stack.pop()
    if (not stack):
        return True
    return False


# exp='(()()())'
exp = '()()(()'
if balanced_stack(exp):
    print('true')
else:
    print('false')
