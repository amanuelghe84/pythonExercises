import json
import yaml
import csv


def starts_with_vowel(word):
    return word[0].lower() in 'aeiou'

def filter_words_starting_with_vowel(words):
    return [word for word in words if starts_with_vowel(word)]

print(filter_words_starting_with_vowel(words))





dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40 }
]

def extract_values(dicts, key):
    return [d[key] for d in dicts if key in d]

print(extract_values(dicts, "name"))




def word_lengths_in_list(my_sentence):
    
    return [len(word) for word in my_sentence[0].split()]

my_sentence = ["i am learning the full stack boot camp"]
result = word_lengths_in_list(my_sentence)
print(result) 