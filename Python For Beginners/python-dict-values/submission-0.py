from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    my_list = [] 
    for key in age_dict:
        age = age_dict[key]
        my_list.append(age)
    return(my_list)

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
