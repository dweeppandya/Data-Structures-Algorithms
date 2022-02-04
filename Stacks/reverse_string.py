from stack import Stack

def reverse_string(input_str):
    s = Stack()
    for i in range(len(input_str)):
        s.push(input_str[i])
    rev_str = ''
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str

def main():
    print(reverse_string('Hello World!'))

if __name__ == '__main__':
    main()