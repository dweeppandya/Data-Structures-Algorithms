from stack import Stack

def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0

    s = Stack()
    result = dec_num
    remainder = -1
    while result != 0:
        remainder = result % 2
        s.push(remainder)
        result = result // 2
    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

def main():
    print(convert_int_to_bin(242))

if __name__ == '__main__':
    main()