def alternate_characters(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)

def alternate_words(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)

# Example usage
input_string1 = "Hello World"
input_string2 = "I am learning to code"

print("Alternate Characters:", alternate_characters(input_string1))
print("Alternate Words:", alternate_words(input_string2))
