def my_filter(function, iterable):
    """
    This function runs over an iterable and return only the item that is true
    according to another function that is passed by argument.
    :param function: Function to send it the iterable items and check whether they are true or false.
    :param iterable: Iterable to go over it.
    :return: Filtered items.
    """
    for item in iterable:
        if function(item) is True:
            yield item
