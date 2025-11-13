# doctest: +ELLIPSIS

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' '
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе.

    >>> encode('SOS')
    '... --- ...'

    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'

    >>> encode('INVALID!')
    Traceback (most recent call last):
    ...
    KeyError: '!'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
