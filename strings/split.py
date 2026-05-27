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
    
    >>> split("a,b,c", separator=",")
    ['a', 'b', 'c']
    
    >>> split("hello world foo bar", separator=" ")
    ['hello', 'world', 'foo', 'bar']
    
    >>> split("onetwoonetwothree", separator="two")
    ['one', 'one', 'three']
    
    >>> split("", separator="x")
    ['']
    
    >>> split("aaa", separator="a")
    ['', '', '', '']
    """

    split_words = []
    last_index = 0
    sep_len = len(separator)
    
    if sep_len == 0:
        return list(string)
    
    index = 0
    while index <= len(string) - sep_len:
        if string[index:index + sep_len] == separator:
            split_words.append(string[last_index:index])
            last_index = index + sep_len
            index += sep_len
        else:
            index += 1
    
    split_words.append(string[last_index:])
    
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
