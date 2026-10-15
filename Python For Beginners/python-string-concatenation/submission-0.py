def concatenate(s1: str, s2: str) -> str:
    combine = s1 + s2 
    if(len(combine) > 10):
        return("Too long!")
    return(combine)




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
