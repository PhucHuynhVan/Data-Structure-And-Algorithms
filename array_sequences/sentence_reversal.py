"""Sentence Reversal"""


def sentence_reversal_func(sentence: str):
    """sentence_reversal_func"""
    i = 0
    length = len(sentence)
    words = []
    spaces = [" "]
    while i < length:

        if sentence[i] not in spaces:
            word_start = i
            while i < length and sentence[i] not in spaces:
                i += 1
            words.append(sentence[word_start:i])

        i += 1

    return " ".join(reversed(words))
