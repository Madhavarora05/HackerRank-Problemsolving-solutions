# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38 , no rounding occurs as the result will still be a failing grade.
def gradingStudents(grades):
    for i in grades:
        if i<38:
            print(i)
        elif (i+1)%5==0 or (i+2)%5==0:
            if (i+1)%5==0:
                print (i+1)
            else:
                print(i+2)
        else:
            print(i)
if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)