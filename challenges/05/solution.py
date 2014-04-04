#!/usr/bin/env python3

import sys

ALPHABET = tuple(map(chr, range(97, 123)))
ALPHABET = tuple(map(lambda x: str.upper(x), ALPHABET))

def ceaser_output(number):
    def ceaser_output_decorator(original_function):
        def wrapper(*args, **kwargs):
            shifted_text = []
            for character in original_function(*args, **kwargs):
                if str.isalpha(character):
                    letter = str.upper(character)
                    letter_number = ALPHABET.index(letter)
                    shifted_letter = ALPHABET[(letter_number + number) % 26]
                    shifted_text.append(shifted_letter)
                else:
                    shifted_text.append(character)
            return "".join(shifted_text)
        return wrapper
    return ceaser_output_decorator


def ceaser_input(number, filter_function):
    def ceaser_input_decorator(original_function):
        def wrapper(*args, **kwargs):
            shifted_text = []
            print('*args is', " ".join(args))
            words_to_shift = [arg for number, arg in enumerate(args) if
                    filter_function(number)]
            words_frozen = [ arg for number, arg in enumerate(args) if not
                    filter_function(number)]
            print('words to shift:', " ".join(words_to_shift))
            print('words frozen:', " ".join(words_frozen))
            for index, word in enumerate(args):
                print('index', index)
                if filter_function(index):
                    shifted_word = ''
                    for character in word:
                        print('character', character)
                        if str.isalpha(character):
                            shifted_letter = ALPHABET[(ALPHABET.index(str.upper(character)) + number) %
                                                     26]
                            shifted_word += shifted_letter
                        else:
                            shifted_word += character
                    shifted_text.append(shifted_word)
                else:
                    shifted_text.append(word)
            #text_to_return = words_frozen + shifted_text
            print('shifted text', shifted_text)
            return original_function(" ".join(shifted_text[:1]),
                    " ".join(shifted_text[1:]))
        return wrapper
    return ceaser_input_decorator

@ceaser_input(-13, lambda key: key > 2)
def make_a_speech(name, *args):
    print('{} says:\n{}'.format(name, ' '.join(args)))

make_a_speech('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                          'RIRE', 'QBAR', 'SBE', 'HF?', '...')
