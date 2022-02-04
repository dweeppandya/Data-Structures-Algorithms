from stack import Stack

def is_match(s1, s2):
    if s1 == '(' and s2 == ')':
        return True
    elif s1 == '[' and s2 == ']':
        return True
    elif s1 == '{' and s2 == '}':
        return True
    return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '([{':
            s.push(paren)
        elif paren in ')]}':
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    return False

def main():
    print(is_paren_balanced('(([[]]))'))
    print(is_paren_balanced('(([[]))'))
    print(is_paren_balanced('(([[asdasdfsdf]adsad])){}'))

if __name__ == '__main__':
    main()