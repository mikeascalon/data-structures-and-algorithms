from data_structures.queue import Queue


def multi_bracket_validation(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
