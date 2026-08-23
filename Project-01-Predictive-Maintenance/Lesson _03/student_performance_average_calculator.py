score_1= float(input("Enter the first score: "))
if score_1 < 0 or score_1 > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    score_2= float(input("Enter the second score: "))
    if score_2 < 0 or score_2 > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        score_3= float(input("Enter the third score: "))
        if score_3 < 0 or score_3 > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            average_score= (score_1+score_2+score_3)/3
            if average_score >=90 and average_score <=100:
                print("Your Result is : Outstanding.")
            elif average_score >=70 and average_score <90:
                print("Your Result is : Distinction.")
            elif average_score >=60 and average_score <70:
                print("Your Result is : Merit.")
            elif average_score >=50 and average_score <60:
                print("Your Result is : Pass.")
            elif average_score >=0 and average_score <50:
                print("Your Result is : Fail.")
            else:
                print("Invalid score. Please enter a score between 0 and 100.")