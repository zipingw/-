def bracketMatch(s):
    stack = []
    print(s)
    for i, char in enumerate(s):
        if char == '(':
            stack.append((char, i))
        elif char == ')':
            if stack:
                item = stack[-1]
                if item[0] == '(':
                    stack.pop()
                else:
                    stack.append((char, i))
            else:
                stack.append((char, i))

    if not stack:
        print()
        return

    res = [' '] * len(s)
    for char, idx in reversed(stack):
        res[idx] = char

    for char in res:
        if char == ' ':
            print(char, end='')
        elif char == ')':
            print('?', end='')
        elif char == '(':
            print('x', end='')

    print()


if __name__ == '__main__':
    bracketMatch("))))))))))))")
    bracketMatch("bge)))))))))")
    bracketMatch("((IIII))))))")
    bracketMatch("()()()()(uuu")
    bracketMatch("))))UUUU((()")
