def divide_numbers(a: str, b: str) -> None:
    try:
        int_a = int(a)
        int_b = int(b)
        result = int_a/int_b
        print(result)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occured:", error)


# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
