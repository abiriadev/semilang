def lexer(code):
    stack = []
    i = 0
    n = 0
    isN = False

    while len(code) > i:
        if code[i] == ';':
            if isN:
                stack.append(n)
                n = 0
                isN = False
            else:
                print("Syntax Error ; semicolon is not have number")
                exit(0)
        elif code[i] == ':':
            if len(stack) < 1:
                print("Error : Stack is Empty")
                exit(0)
            else:
                stack.pop()
        elif code[i] == '+':
            if len(stack) < 2:
                print("Error + Stack is Empty")
                exit(0)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
        elif code[i] == '-':
            if len(stack) < 2:
                print("Error + Stack is Empty")
                exit(0)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a-b)
        elif code[i] == '!':
            if len(stack) < 1:
                print("Error : Stack is Empty")
                exit(0)
            else:
                print(stack.pop(), end='')
        elif code[i] == '@':
            if len(stack) < 1:
                print("Error : Stack is Empty")
                exit(0)
            else:
                print(chr(stack.pop()), end='')
        elif code[i] >= '0' and code[i] <= '9':
            n = n*10 + int(code[i])
            isN = True
        elif code[i] == '#':
            while len(code) > i and code[i] != '\n':
                i += 1
        i += 1

if __name__ == "__main__":

	code = input("semi > ")

	lexer(code)
    
