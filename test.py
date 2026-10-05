#PRACTICAL EXERCICSES:
#exercise 1
input_string = input("Enter a string: ")
modified_string = input_string.replace(" ", "-")
modified_string = modified_string.upper()
print("Modified string:", modified_string)
print("Length of the string:", len(modified_string))
print()
#exercice2:
sentence = input("Enter a sentence: ")
words_list = sentence.split()
print("List of words:", words_list)
print("First character:", sentence[0])
print("last character:", sentence [-1])
print()
#exercise3:
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}."
print(formatted_string)
print()



#ADVANCED PRACTICE AND MINI PROJECT
sentence = input("Enter a sentence: ")
num_characters = len(sentence)
num_words = len(sentence.split())
print(f"Total characters: {num_characters}")
print(f"Total words: {num_words}")

reversed_sentence = sentence[::-1]
print(f"Reversed sentence: {reversed_sentence}")

word_to_find = input("Enter a word to find its position: ")
position = sentence.find(word_to_find)
if position != -1:
    print(f"The position of '{word_to_find}': {position}")
else:
    print(f"'{word_to_find}' was not found in the sentence.")


vowels = "AEIOUaeiou"
modified_sentence = ''.join(['*' if char in vowels else char for char in sentence])
print(f"Sentence with vowels replaced: {modified_sentence}")
print()
# Bonus:
def to_pig_latin(word):
    vowels = "AEIOUaeiou"
    if word[0] in vowels:
        return word + "yay"
    else:
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + "ay"
        return word 
pig_latin_sentence = ' '.join([to_pig_latin(word) for word in sentence.split()])
print(f"Pig Latin sentence: {pig_latin_sentence}")