def count_vowels(word):
    # Define the vowels
    vowels = "aeiou"
    # Count the number of vowels in the word
    vowel_count = sum(1 for char in word if char in vowels)
    return vowel_count

def main():
    # Accept a sentence in lowercase
    sentence = input("Enter a sentence in lowercase: ")
    
    # Split the sentence into words
    words = sentence.split()
    
    # Display the header
    print("Word\t\t\tNo. of vowels")
    
    # Process each word
    for word in words:
        # Get the vowel count for the word
        vowel_count = count_vowels(word)
        
        # Display the word and its vowel count
        print(f"{word.capitalize()}\t\t\t{vowel_count}")

# Run the program
if __name__ == "__main__":
    main()




