"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # text_file = open(file_path)
    # text = text_file.read()
    # text_file.close()
    # return text

    with open(file_path) as text_file:
        text = text_file.read()

    return text


def make_chains(file_as_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = file_as_string.split()
    words.append(None)
    
    #otherway

    # for i in range(len(words) - 1):
    #     chains[words[i], words[i + 1]] = []

    # for word1, word2 in chains:
    #     for i in range(len(words) - 2):
    #         if words[i] == word1 and words[i + 1] == word2:
    #             chains[(word1, word2)].append(words[i + 2])

    # return chains

    # for i in range(len(words)-2):
    #     key = (words[i], words[i+1])
    #     value = words[i+2]
    #     chains[key] = chains.get(key, [])
    #     chains[key].append(value)

    # return chains

    for i in range(len(words)-n):
        key = []
        for j in range(n):
            key.append(words[i + j])
        key = tuple(key)
        value = words[i+n]
        chains[key] = chains.get(key, [])
        chains[key].append(value)

    return chains

def make_text(chain):
    """Return text from chains."""

    start_key = choice(chain.keys())
    print start_key
    # start_key1, start_key2 = key
    # words = [start_key1, start_key2]
    words = list(start_key)

    while True:
        next_word = choice(chain[start_key])
        if not next_word:
            break
        start_key2 = list(start_key)
        start_key2.pop(0)
        start_key2.append(next_word)
        print start_key2
        words.append(next_word)
        print words


    return " ".join(words)


filename = sys.argv[1]
file_as_string = open_and_read_file(filename)
my_chain = make_chains(file_as_string, 5)
print make_text(my_chain)



# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
