def form_word_from_first_chars(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Extract the first character of each word and join them
    new_word = ''.join([word[0] for word in words])
    
    return new_word

# Input a sentence
sentence = input("Enter a sentence: ")

# Form the new word and display it
new_word = form_word_from_first_chars(sentence)
print("The word formed by joining the first characters of each word is:", new_word)
