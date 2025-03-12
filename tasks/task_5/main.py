def count_vowels_consonants(text):
    vowels = "AEIOUaeiou"
    vowel = 0
    consonant = 0

    for char in text:
        if char.isalpha(): 
            if char in vowels:
                vowel += 1
            else:
                consonant += 1
    return vowel, consonant

text = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
