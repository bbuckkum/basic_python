def grader(name, score) :
    if 95 <= score <= 100 :
        grade = "A+"
    elif 90 <= score <= 95 :
        grade = "A"
    elif 85 <= score <= 89 :
        grade = "B+"
    elif 80 <= score <= 84 :
        grade = "B"
    elif 75 <= score <= 79 :
        grade = "C+"
    elif 70 <= score <= 74 :
        grade = "C"
    elif 65 <= score <= 69 :
        grade = "D+"
    elif 60 <= score <= 64 :
        grade = "D"
    else :
        grade = "F"

    print("학생이름 : ", name)
    print("점수 : ", score)
    print("학점 : ", grade)
    return grade


nm = input("이름을 입력하시오 : ")
sr = input("점수를 입력하시오 : ")
inm = str(nm)
isr = int(sr)

grader(inm, isr)