# Problem: Given a list of size n, remove all even integers from it. 
# Input: A list with random integers.
# Output: A list with only odd integers
# Sample Input: my_list = [1,2,4,5,10,6,3]
# Sample Output: my_list = [1,5,3]

def remove_even(lst):
    # Time Complexity: O(n)
    # Using List comprehension
    return [num for num in lst if num%2 != 0]

def main():

    # test case 1
    lst = []
    print(remove_even(lst))

    # test case 2
    lst = [
        169, 167, 158, -99, -137, -199, 157, 101, -91, -17, -9, -26, -140, -142, 74,
        -144, -52, 134, 63, 18, 145, 39, -56, 177, -87, -42, -67, 69, 190, -64, 35, 75, 100,
        30, -60, -129, -126, -103, -55, -152, -13, 49, 9, 58, -4, 62, -186, -169, -12, 102,
        -182, 89, 88, 72, -128, -80, 95
    ]
    print(remove_even(lst))

if __name__ == '__main__':
    main()