def leap_year(leap_year):
    if leap_year%4==0:
        if leap_year%100==0:
            if leap_year%400==0:
                print("leap_year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")
leap_year(2400)
        