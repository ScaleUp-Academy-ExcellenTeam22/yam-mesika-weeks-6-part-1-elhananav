def get_positive_numbers():
    """
    This function get series of numbers separated by a comma from the user, and return
    all the positive numbers as int list.
    """
    val = input("Enter a series of numbers separated by a comma:\n").split(",")
    int_val = map(lambda n: int(n), val)
    return list(filter(lambda n: n >= 0, int_val))


if __name__ == "__main__":
    print(get_positive_numbers())
