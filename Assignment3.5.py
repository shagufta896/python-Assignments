# Accept a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the order of words
reversed_sentence = ' '.join(reversed(words))

# Display the reversed sentence
print("Reversed sentence:", reversed_sentence)
