def full_names(first_names, last_names, min_length=0):
    """
    The function receives as parameters a list of first names and a list of last names,
    and compiles full names from them. For each first name, the function will attach all
    the family names received.
    :param first_names: List of first names.
    :param last_names: List of last names.
    :param min_length: To filter the full names to those that bigger than this parameter(optional).
    :return: List of full names.
    """
    full_names1 = [first_name.title() + ' ' + last_name.title()
                   for first_name in first_names for last_name in last_names]
    if min_length == 0:
        return full_names1
    return list(filter(lambda name: len(name) >= min_length, full_names1))


if __name__ == "__main__":
    first_names1 = ['avi', 'moshe', 'yaakov']
    last_names1 = ['cohen', 'levi', 'mizar']
    print(full_names(first_names1, last_names1, 10))
    print(full_names(first_names1, last_names1))
