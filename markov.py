"""Generate markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    reader = open("green-eggs.txt").read()

    return reader


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

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
    """

    
    chains = {}
    text = text_string.split()
    text_len = len(text)


    for word in range(text_len-2):

        key = (text[word], text[word + 1])
        value = text[word+2]

        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]
    
        
    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    word_generator = choice(name of list)
    words.append(word_generator)
    print words

    your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
