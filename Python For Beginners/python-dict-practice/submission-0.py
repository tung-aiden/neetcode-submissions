from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dicty = {}
    for char in word: 
        if char not in dicty:
            dicty[char] = 0
        if char in dicty:
            dicty[char] += 1
    return(dicty)
    




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
