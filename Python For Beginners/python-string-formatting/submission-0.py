def say_goodbye(name: str, hour: int) -> str:
    message = f"Goodbye, {name}. See you again at {hour} o'clock."
    return(message)

# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))
