# using a for loop in python
# A for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
# Creating a list
scores = [70,85,92,78,74,88]
# iterating over the list using a for loop
for score in scores:
    print(score)
    # modifying the loop
for score in scores:
    print(f"Score :{score}")
     
# modifying the loop to print only scores greater than 70

for score in scores:
    if score >70:
        print(f"score : {score}")
# caLculte the total and average of the scores using a for loop
total=0
for score in scores:
    total+=score
average= total/len(scores)
print(f"Total : {total}")
print(f"Average : {average}")
# to count how many scores are in the list that is greater than 70
count=0
for score in scores:
    if score>=70:
        count+=1

print(f"the list contains a total of {count} scores that are greater than 70")
# to print the highest score
highest_score=scores[0]
for score in scores:
    if score >highest_score:
        highest_score=score
print(f"The highest score is : {highest_score}")

# to print the lowest score
lowest_score=scores[0]
for score in scores:
    if score <lowest_score:
        lowest_score=score
print(f"The lowest score is : {lowest_score}")
    