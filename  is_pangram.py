# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

from string import ascii_lowercase as alphabet

def is_pangram(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.replace(' ', '').lower()
    return alphabet.issubset(set(s))

def is_pangram1(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.replace(' ', '').lower()
    return all(letter in s for letter in alphabet)

def is_pangram2(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.replace(' ', '').lower()
    return len(alphabet - set(s)) == 0

def is_pangram3(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.replace(' ', '').lower()
    return not alphabet.difference(set(s))

is_pangram = lambda s: set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

def is_pangram4(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    st_set = set(s.lower())
    for el in alphabet:
        if el not in st_set:
            return False
    return True

def is_pangram5(s:str) -> bool:
    # alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(alphabet) <= set(s.lower())

print(is_pangram5("The quick brown fox jumps over the lazy dog."))
