from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_arr = []
    for i in range(len(arr)):
        number = arr.pop()
        new_arr.append(number)
    return(new_arr)



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
