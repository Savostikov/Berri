vowels = set('aeiou')
word = input("Provide a word to search for vovels:")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
b