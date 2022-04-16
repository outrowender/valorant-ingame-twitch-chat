import random


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def generateRandomNumbers():
    randomlist = random.sample(range(0, 9), 5)
    return ''.join(map(str, randomlist))
