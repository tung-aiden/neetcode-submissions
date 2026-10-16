def add_two_numbers() -> int:
    ints = input()
    seperate = ints.split(",")
    sum = 0
    for i in seperate: 
        sum += int(i)
    return(sum)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
