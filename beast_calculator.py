def beast_func():
    num_from_word = []
    output_sum = input("Enter word to calculate: ")

    for letter in output_sum:
        num_from_word.append(ord(letter) - 96)

    return sum(num_from_word)


print(beast_func())
