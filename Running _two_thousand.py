import time


def timer(f, *args, **kwargs):
    """
    Function receives function parameter and its parameters, and measure how long
    it took the passed function to run.
    :param f: Function to measure its run time.
    :param args: Unnamed parameters for the measured function.
    :param kwargs: Named parameters for the measured function.
    :return: The time it took for the function to run.
    """
    start_time = time.time()
    f(*args, **kwargs)
    return time.time() - start_time


if __name__ == "__main__":
    print(timer("Hi {name}".format, name="Bug"))
