"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    your_file = open(file_path).read()
    return your_file


file_as_string = open_and_read_file('green-eggs.txt')


def make_chains(file_as_string):
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

    for i in range(len(words) - 1):
        chains[words[i], words[i + 1]] = []

    for word1, word2 in chains:
        for i in range(len(words) - 2):
            if words[i] == word1 and words[i + 1] == word2:
                chains[(word1, word2)].append(words[i + 2])

    return chains


my_chain = make_chains(file_as_string)


def make_text(chain):
    """Return text from chains."""

    starting_word = choice(chain.keys())

    while True:
        next_word = choice(chain[starting_word])
        if not next_word:
            break
        first_word, second_word = starting_word
        starting_word = (second_word, next_word)









    print starting_word
    print next_word
    # return " ".join(words)


make_text(my_chain)





# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
