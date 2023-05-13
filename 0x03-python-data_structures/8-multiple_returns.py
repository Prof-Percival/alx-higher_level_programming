#!/usr/bin/python3
def multiple_returns(sentence):
    length_sentence = len(sentence)

    if (length_sentence == 0):
        new_tuple = (length_sentence, None)
    else:
        new_tuple = (length_sentence, sentence[0])

    return (new_tuple)
