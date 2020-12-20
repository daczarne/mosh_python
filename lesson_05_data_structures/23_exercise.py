from pprint import pprint

# Find the most common character in a text
sentence = "This is a common interview question"

# generate a dictionary where each letter is a key and it's value is it's frequency
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

# sort the dictionary
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True
)

print(char_frequency_sorted[0])
