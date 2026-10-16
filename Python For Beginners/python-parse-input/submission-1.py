from typing import List

def read_integers() -> List[int]:
    ints = input()
    listy = ints.split(",")
    int_list = []
    for x in listy:
        int_list.append(int(x))
    return(int_list)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
