def words_length(sentence):
    """
    This function gets a sentence and return a list of all word's length.
    :param sentence: Sentence to return its word's length.
    :return: list of word's length.
    """
    return [len(word) for word in sentence.split(" ")]


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
