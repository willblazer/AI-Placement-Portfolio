scores = [70,85,92,78,74,88]

# caLculte the total , average of the scores,total number of scores,highest and lowest scores using a for loop
total=0
for score in scores:
    total+=score
num_of_scores=0
for score in scores:
        num_of_scores+=1
average= total/num_of_scores
print(f"Total : {total}")
print(f"Average : {average}")
# to count how many scores are in the list that are equal to or greater than 70
count=0
for score in scores:
    if score>=70:
        count+=1

print(f"the list contains a total of {count} scores that are equal to or greater than 70")
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
    