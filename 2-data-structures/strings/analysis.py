# Exercise 8: String Manipulation
text = "Hello, World!"
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)
print(f'vowels: {vowel_count}, consonants: {consonant_count}')
