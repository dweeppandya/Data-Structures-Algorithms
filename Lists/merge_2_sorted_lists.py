# Problem: Given two sorted lists, merge them into one list which should also be sorted.
# Input: Two sorted lists.
# Output: A merged and sorted list consisting of all elements of both input lists.
# Sample Input: 
#   list1 = [1,3,4,5]  
#   list2 = [2,6,7,8]
# Sample Output: 
#   arr = [1,2,3,4,5,6,7,8]


def merge_lists_method1(lst1, lst2):
    # Creating a new list
    # Time Complexity: O(n + m)

    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1

    return_lst = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            return_lst.append(lst1[i])
            i += 1
        else:
            return_lst.append(lst2[j])
            j += 1

    while i < len(lst1):
        return_lst.append(lst1[i])
        i += 1

    while j < len(lst2):
        return_lst.append(lst2[j])
        j += 1

    return return_lst


def merge_lists_method2(lst1, lst2):
    # Merging in place
    # Time Complexity: 
    #   O(m^2) if m > n
    #   O(n^2) if n >m
    # Space Complexity: O(m) i.e. more efficient than method 1

    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            # Insert list2's current element to list1
            lst1.insert(i, lst2[j])
            i += 1
            j += 1
        else:
            i += 1

    if j < len(lst2):
        lst1.extend(lst2[j: ])

    return lst1


def main():
    # test case 1
    list1 = [1,3,4,5]  
    list2 = [2,6,7,8]
    print("Test Case 1: ")
    print(merge_lists_method1(list1, list2))
    print(merge_lists_method2(list1, list2))
    print()

    # test case 2
    list1 = []
    list2 = [1, 2, 3, 4, 5]
    print("Test Case 2: ")
    print(merge_lists_method1(list1, list2))
    print(merge_lists_method2(list1, list2))



if __name__ == '__main__':
    main()