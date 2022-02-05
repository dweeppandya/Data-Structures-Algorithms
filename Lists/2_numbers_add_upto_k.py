# Problem: Given a list and a number "k", find two numbers from the list that sum to "k".
# Input: A list and a number k
# Output: A list with two integers a and b that add up to k
# Sample Input:
#   lst = [1,21,3,14,5,60,7,6]
#   k = 81
# Sample Output:
#   lst = [21,60]


def find_sum_method1(lst, k):
    # Brute force
    # Time Complexity: O(n^2)
    if len(lst) == 0 or len(lst) == 1:
        return

    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == k:
                return [lst[i], lst[j]]
            j += 1
        i += 1


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    index = -1

    while first <= last and not found:
        mid = (first + last)//2
        if lst[mid] == item:
            index = mid
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    return -1

def find_sum_method2(lst, k):
    # Using a sort list and binary search
    # Time Complexity: O(nlogn)
    lst.sort()
    for j in range(len(lst)):
        index = binary_search(lst, k - lst[j])
        if index != -1 and index != j:
            return [lst[j], k - lst[j]]


def find_sum_method3(lst, k):
    # Sort the list and use moving indices
    # Time Complexity: O(nlogn) + O(n) = O(nlogn)
    lst.sort()
    i = 0
    j = len(lst) - 1
    summation = 0
    while i != j:
        summation = lst[i] + lst[j]
        if summation < k:
            i += 1
        elif summation > k:
            j -= 1
        else:
            return [lst[i], lst[j]]
    return False


def main():
    print(find_sum_method1([1, 2, 3, 4], 5))
    print(find_sum_method2([1, 2, 3, 4], 5))
    print(find_sum_method3([1, 2, 3, 4], 5))


if __name__ == '__main__':
    main()