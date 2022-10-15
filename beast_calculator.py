beast_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 8, 'k': 9, 'l': 10, 'm': 11,
              'n': 12, 'o': 13, 'p': 14, 'q': 15, 'r': 16, 's': 17, 't': 18, 'u': 19, 'v': 20, 'w': 21, 'x': 22,
              'y': 23, 'z': 24}


def beast_func(word1):
    output_sum = ""
    dict_values = "beast_dict.values()"
    for num in word1:
        if num in dict_values:
            output_sum = sum(output_sum)
    return output_sum


print(beast_func(input("Enter word to calculate: ")))
