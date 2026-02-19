def get_character_frequencies(input_string):
    frequencies = {}

    for char in input_string:
        char = char.lower()  # Convert to lowercase for case-insensitive counting
        if char in frequencies:
            frequencies[char] += 1
            print("Got a new character: " + char)
        else:
            frequencies[char] = 1
    return frequencies

mydict = get_character_frequencies("Snow White and the Seven Dwarves")

print(mydict)
sorted_by_keys = dict(sorted(mydict.items()))
print(sorted_by_keys)