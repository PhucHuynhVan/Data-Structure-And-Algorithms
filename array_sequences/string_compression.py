"""String Compression"""


def string_compression_func(string: str) -> str:
    """String Compression Func"""
    compressed_str = ""
    length = len(string)
    # The edge case when string is empty
    if length == 0:
        return ""
    # The edge case when string is only one character
    if length == 1:
        return string + str(1)
    count = 1
    i = 1
    while i < length:

        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_str = compressed_str + string[i-1] + str(count)
            count = 1
        i += 1

    compressed_str = compressed_str + string[i-1] + str(count)
    return compressed_str
