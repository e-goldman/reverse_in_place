# reverse_in_place
Simple exercise 1 - Reverse words in place

Source: Interview Cake

Premise:

Given a sentence in which the words are correct but in backwards order, reverse the word order so the message is legible. 
For example, given 'rad is learning machine', it should read 'machine learning is rad'.

The message is presented as a list of characters, and they must be reversed in place. Time cost must be O(n).

Typically such a message would be stored as a string, but because the object of the exercise is to perform the reversal in place, 
the input needs to be in a mutable type.

This is my solution. It uses a helper function that reverses the characters between two indices to correct the message in
two stages:

1) Reverse the whole message. The above example would now read 'enihcam gninrael si dar'.
2) Reverse each word, delineated by the spaces between them.
