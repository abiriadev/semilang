def calculating(cal):
    value = cal[0]
    i = 1
    while len(cal) > i+1:
        if cal[i] == '+':
            i += 1
            if cal[i] == '+' or cal[i] == '-':
                print("Syntax Error ; Double operator")
                exit(0)
            value += cal[i]
        elif cal[i] == '-':
            i += 1
            if cal[i] == '+' or cal[i] == '-':
                print("Syntax Error ; Double operator")
                exit(0)
            value -= cal[i]
        i += 1
    cal.clear()
    return value

def lexer(code):
    stack = []
    cal = []
    i = 0
    n = 0
    isN = False

    while len(code) > i:
        if code[i] == ';':
            if isN:
                cal.append(n)
                n = 0
                isN = False
            stack.append(calculating(cal))
        elif code[i] == ':':
            if len(stack) == 0:
                print("Error ; Stack is Empty")
                exit(0)
            else:
                im = stack[len(stack)-1]
                if isN:
                    cal.append(str(n)+im)
                    n = 0
                    isN = False
                else:
                    cal.append(im)
        elif code[i] == '.':
            if isN:
                cal.append(n)
                n = 0
                isN = False
            if len(stack) == 0:
                print("Error ; Stack is Empty")
                exit(0)
            else:
                stack.pop()
        elif code[i] == '+':
            if isN:
                cal.append(n)
                n = 0
                isN = False
            cal.append('+')
        elif code[i] == '-':
            if isN:
                cal.append(n)
                n = 0
                isN = False
            cal.append('-')
        elif code[i] == '!':
            if isN:
                cal.append(n)
                n = 0
                isN = False
            print(calculating(cal))
        elif code[i] >= '0' and code[i] <= '9':
            n = n*10 + int(code[i])
            isN = True
        i += 1

lexer("20;10;:.+:+10+10+10!")

lexer("")