def display_patterns(word):
    length = len(word)
    
    # First Pattern
    print("First Pattern:")
    for i in range(length):
        # Print the current character repeated (i + 1) times
        print("  ".join([word[i]] * (i + 1)))
    
    # Second Pattern
    print("\nSecond Pattern:")
    for i in range(length, 0, -1):
        # Print the word up to the i-th character
        print("  ".join(list(word[:i])))

# Input a word
word = input("Enter a word: ").upper()

# Display the patterns
display_patterns(word)