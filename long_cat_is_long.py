import re


def count_words(text):
    """
    This function receives text as a parameter, and returns a dictionary of the word lengths in it.
    :param text: The text that will become a dictionary.
    :return: A dictionary of the word lengths in it.
    """
    only_words = (re.sub(r'[^a-zA-Z]', '', word) for word in text.split())
    return {word: len(word) for word in only_words}


if __name__ == "__main__":
    text1 = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text1))

