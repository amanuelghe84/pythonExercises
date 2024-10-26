
# Python Code Challenge: Functions and List Comprehensions

# Challenge 1: Define a function that takes a list of numbers and returns a new list containing only the even numbers.
# The function should use list comprehension.
numbers = [i for i in range(10) ]

print(numbers)

numbers = [i for i in range(10) if i % 2 == 0]

print("even_numbers:", numbers)

print("-----------------------1111--------------------------------")
# Challenge 2: Define a function that takes a list of strings and returns a new list with the strings that have more than 5 characters.
# Use list comprehension for filtering.


fruits = ["banana", "grape", "apple", "watermelon", "orange"]


long_fruits = [fruit for fruit in fruits if len(fruit) > 5]

print(long_fruits)


print("----------------------2222------------------------------------")
 
# Challenge 3: Write a function that takes a list of integers and returns a list of their squares.
# Use list comprehension to achieve this.

num_list = [1, 2, 3, 4, 5, 6]

num_list = [i**2 for i in range(5) if i >= 1 ]

print(num_list)

print("----------------------3333------------------------------------")

# Challenge 4: Write a function that accepts two lists of the same length and returns a list of tuples,
# where each tuple contains elements from the two lists at the corresponding positions. Use list comprehension.

list1 = [1, 2, 3, 4, 5, 6]

list2 = ["a", "b", "c", "d", "e", "f"]

def com_lists(list1, list2):

    return [(list1[i],list2[i]) for i in range(len(list1))]

result = com_lists(list1, list2)

print(result)

print("----------------------4444-----------------------------------")


# Challenge 5: Create a function that takes a sentence (string) and returns a list of the lengths of each word in the sentence.
# Use list comprehension to split the sentence and calculate the lengths.

my_sentence = ["i am learning the full stack boot camp"]


print("---------------------5555------------------------------------")

# Challenge 6: Define a function that filters out words from a list that do not start with a vowel.
# Use list comprehension and a helper function that checks if a word starts with a vowel.

words = ["amanuel", "yonas", "awet", "robel", "teame"]




print("---------------------6------------------------------------")

# Challenge 7: Write a function that takes a list of numbers and returns a list of booleans indicating whether each number is greater than 10.
# Use list comprehension for this task.

numbers = [2, 3, 15, 7, 19, 20, 13, 5, 17]

def list_of_numbers(numbers):
    return [number > 10 for number in numbers]
result = list_of_numbers(numbers)
print(result)

print("----------------------7777------------------------------------")

# Challenge 8: Create a function that takes a list of dictionaries and returns a list of the values for a given key.
# Use list comprehension to extract the values.




print("----------------------888------------------------------------")
# Challenge 9: Write a function that accepts a list of words and returns a list of the words with their first letter capitalized.
# Use list comprehension to achieve this.

words = ["hello", "world"]

def capitalize_words(words):
    return[word.capitalize() for word in words]
result = capitalize_words(words)

print(result)

print("----------------------999------------------------------------")
# Challenge 10: Write a function that returns the common elements between two lists.
# Use list comprehension and the "in" operator to find common elements.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 5, 7, 8, 9 ]

def common_elements(list1, list2):
    return [item for item in list1 if item in list2]
result = common_elements(list1, list2)
print(result)


print("-----------------------10-----------------------------------")