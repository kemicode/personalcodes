#Name: Oluwakemi LaBadie
#Course number: COP1000
#Write a Python program that determines the average of three test scores.
#
#Pseudocode
#Start Program
#Enter the first test score, assign variable 'test_1'
#Enter the second test score, assign variable 'test_2
#Enter the third test score, assign variable 'test_3'
#input average = test_1 + test_2 +  test_3 // 3.0
#Print average with percentage symbol
#End Program

#start Program

test_1 = float(input('Enter the score for test 1: '))
test_2 = float(input('Enter the score for test 2: '))
test_3 = float(input('Enter the score for test 3: '))
average = (test_1 + test_2 + test_3) / 3.0
average = str(round(average, 2))
Print('The average score is: ', average,'%')


