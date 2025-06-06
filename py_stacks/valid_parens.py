def isValid(s: str) -> bool:
    stack = []
    close_to_open = {")" : "(", "]" : "[", "}" : "{"}
    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

input1 = "[]"
input2 = "{[]}"
input3 = "[](){"

print(isValid(input1))
print(isValid(input2))
print(isValid(input3))