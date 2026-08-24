# using list in python
# A list is a collection of items in a particular order. In Python, lists are written within square brackets [] and can contain items of different data types, including numbers, strings, and other lists. Lists are mutable, meaning that their contents can be changed after they are created.
# Creating a list
scores = [70,85,92,68,74]
print(scores)
# Accessing elements in a list
print(scores[0])  # prints the first element
print(scores[2])  # prints the third element
print(scores[-1]) # prints the last element
# modifying elements in a list
scores[-2]=78
print(scores)
# adding an element to a list
scores.append(88)
print(scores)
# couting the number of elements in a list
number_of_observations = len(scores)
# calculating the sum of the items in a list.
total = sum(scores)
# calculating the average of the items in a list
average_score = total/number_of_observations
print(f"The average score is: {average_score}")
# grading the average score using if-elif-else statements
if average_score >=90:
    print("Outstanding")
elif average_score >=70:
    print("Distinction")
elif average_score >=60:
    print("Merit")
elif average_score >=50:
    print("Pass")
else:
    print("Fail")

