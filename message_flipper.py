# helper function to reverse the elements of a list of characters
def reverse(char_list, start, end):
    left_index = start
    right_index = end

    while left_index < right_index:
        char_list[left_index], char_list[right_index] = char_list[right_index], char_list[left_index]
        left_index += 1
        right_index -= 1


# function to reverse all of the words in a complete message
def reverse_words(message):
    word_start = 0
    reverse(message, word_start, len(message) - 1)

    for index, char in enumerate(message):
        if char == ' ':
            word_end = index - 1
            reverse(message, word_start, word_end)
            word_start = index + 1

        if index == len(message) - 1:
            word_end = index
            reverse(message, word_start, word_end)
