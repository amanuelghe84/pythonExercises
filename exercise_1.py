
# 1. Define two variables, x and y, with values 5 and 10.
#    Perform the following operations and print the results:
#    a) Sum of x and y
#    b) Difference of y and x
#    c) Product of x and y
#    d) Quotient of y by x

x = 5
y = 10
z = 5 + 10

print(z)

d = 10 - 5

print(d)

p = 5 * 10

print(p)

q = 10/5

print(q)

print("--------------------------------1---------------------------------------")

# 2. Define a list of fruits containing "apple", "banana", and "cherry".
#    a) Add "orange" to the list.
#    b) Remove "banana" from the list.
#    c) Print the first and last elements of the list.

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

fruits.pop(1)

# pop by using an index

print(fruits)

# fruits.remove("banana")

first_elem, last_elem = "apple", "cherry"

print(first_elem, last_elem)

print(fruits)

print("------------------------------2------------------------------------------")

# 3. Define a set of numbers containing 1, 2, 3, 4, and 5.
#    a) Add the number 6 to the set.
#    b) Remove the number 3 from the set.
#    c) Check if the numbers 5 and 7 are in the set, and print the results.
#cccccc
numbers_set = {1, 2, 3, 4, 5}

numbers_set = list(numbers_set)

numbers_set.append(6)

numbers_set.remove(3)

numbers_set = set(numbers_set)

print(numbers_set)

print("-----------------------------------3-----------------------------------")


# 4. Define a tuple representing coordinates (10.5, 20.7).
#    a) Print the x (first) and y (second) coordinates separately.

coordinates = (10.5, 20.7)

x, y = coordinates

print(x)
print(y)

print("---------------------------------------4--------------------------------")

# 5. Define a dictionary of student grades, where:
#    - "Alice" has a grade of 85
#    - "Bob" has a grade of 90
#    - "Charlie" has a grade of 78
#    a) Add a new student "David" with a grade of 88.
#    b) Update Alice's grade to 95.
#    c) Print Bob's grade.

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
# a)
grades["David"] = 88

print(grades)
# b)
grades["Alice"] = 95

print(grades)
# c)
bob_grade = 90

print(bob_grade)

# for value in values:
#     print(value)

keys = list(grades.keys())

values = list(grades.values())

for value in values:

    print(value)


# for key, value in zip(keys, values):

# for key, value in zip(keys, values):

    # print(key, value)

# for key, value in grades.items():

#     print(f"{key}: {value}")



    


# 6. Define a variable called `age` with a value of 18.
#    a) Write an if/else statement that checks if the age is 18 or above. 
#    If true, print "You are eligible to vote", otherwise print "You are not eligible to vote".

age = 18

if age >= 18:

    print(f" you are eligible to vote")

else:

    print(f"you are not eligible to vote")



# 7. Define a list of fruits: ["apple", "orange", "grape"].
#    a) Use a `for` loop to print each fruit in the list.

fruits = ["apple", "orange", "grape"]

for fruit in fruits:

    print(fruit)

    

# 8. Define a variable `count` with a value of 5.
#    a) Use a `while` loop to print a countdown from 5 to 1.

count = 5

while count > 0:
    print(count)
    count-=1

# 9. Challenge: Combine lists, sets, dictionaries, and loops.
#    a) Define a list of numbers from 1 to 10.
#    b) Create a set of even numbers from the list using a `for` loop or comprehension.
#    c) Create a dictionary that maps each even number to its square.
#    d) Print the set of even numbers and the dictionary.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)


even_numbers = set()

for number in numbers:
    if number % 2 == 0:
        even_numbers.add(number)

print(even_numbers)


even_numbers_dict = {}

for number in numbers:
    if number % 2 == 0:
        even_numbers_dict[number] = number ** 2

print(even_numbers_dict)        



# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))



# squared = list(map(lambda x: x**2, numbers))






# 10. Conversion between List, Set, and Tuple
#     a) Convert the list of fruits to a set and print the result.
#     b) Convert the set of even numbers to a tuple and print the result.
#     c) Convert the tuple of coordinates to a list and print the result.

# Conversion between list, set, and tuple examples:
# fruits -> set
# even_numbers (from challenge) -> tuple
# coordinates (tuple) -> list

fruits = ["apple", "orange", "grape"]

fruits = set(fruits)

print(fruits)

even_numbers = tuple(even_numbers)

print(even_numbers)

coordinates = (10.5, 20.7)

coordinates = list(coordinates)

print(coordinates)



# 11. Dictionary Keys and Values
#     a) Print the list of dictionary keys from the `grades` dictionary.
#     b) Print the list of dictionary values from the `grades` dictionary.
#     c) Loop through the dictionary and print each student name (key) and their grade (value).

# Dictionary keys and values
# grades -> keys() -> list
# grades -> values() -> list
# loop through dictionary

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

keys = grades.keys()

print(keys)

values = grades.values()

print(values)

items = grades.items()

print(items)
