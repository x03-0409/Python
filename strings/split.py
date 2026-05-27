def split(string: str, separator: str = " ") -> list:
    """
    Will split the string up into all the values separated by the separator
    (defaults to spaces)

    >>> split("apple#banana#cherry#orange",separator='#')
    ['apple', 'banana', 'cherry', 'orange']

    >>> split("Hello there")
    ['Hello', 'there']

    >>> split("11/22/63",separator = '/')
    ['11', '22', '63']

    >>> split("12:43:39",separator = ":")
    ['12', '43', '39']

    >>> split(";abbb;;c;", separator=';')
    ['', 'abbb', '', 'c', '']
    """

    split_words = []

    sep_len = len(separator)
    last_index = 0
    i = 0
    while i <= len(string) - sep_len:
        if string[i : i + sep_len] == separator:
            split_words.append(string[last_index:i])
            last_index = i + sep_len
            i = last_index
            continue
        i += 1
    split_words.append(string[last_index:])
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
