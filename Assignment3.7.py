# Input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Calculate the length of the longest word
longest_word_length = len(longest_word)

# Display the longest word and its length
print("The longest word:", longest_word)
print("The length of the word:", longest_word_length)

