### 10. Create a list with pattern ['a', 'bb', 'ccc', ..., 'zzz...']:

# Create the list with repeated letters
char_list = []
for i in range(26):
    char_list.append(chr(97 + i) * (i + 1))

# Add 26 copies of 'z' at the end
char_list.extend(['z'] * 26)

# Print the final list
print(char_list)

