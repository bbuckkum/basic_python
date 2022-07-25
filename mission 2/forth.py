def bus_fare(age, sort) :
    if 1 <= age < 8 :
        fare = "무료"
    elif 8 <= age < 14 :
        fare = "450원"
    elif 14 <= age < 20 :
        if sort == "카드" :
            fare = "720원"
        elif sort == "현금" :
            fare = "1000원"
    elif 75<= age :
        fare = "무료"
    elif 20 <= age :
        if sort == "카드" :
            fare = "1200원"
        elif sort == "현금" :
            fare = "1300원"

    print("나이 : ", age)
    print("지불유형 : ", sort)
    print("버스요금 : ", fare)
    return fare

age = int(input("나이를 입력하시오. : "))
sort = input("현금인가요? 카드인가요? :")

bus_fare(age, sort)