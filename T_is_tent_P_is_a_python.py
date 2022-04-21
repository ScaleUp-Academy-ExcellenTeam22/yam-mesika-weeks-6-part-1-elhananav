def get_letters():
    """
    This function return list all the characters between a and z and between A and Z.
    :return: A list of all lowercase and uppercase letters.
    """
    a2z = [chr(lower_letter) for lower_letter in range(ord('a'), ord('z') + 1)]
    A2Z = [chr(upper_letter) for upper_letter in range(ord('A'), ord('Z') + 1)]
    return a2z + A2Z


if __name__ == "__main__":
    print(get_letters())
