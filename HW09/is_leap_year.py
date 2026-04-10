def is_leap_year():
    year = int(input("년도를 입력해주세요"))
    if year % 4 == 0 and year % 100 != 0 :
        print(f"{year}은 윤년입니다")
    else :
        print(f"{year}은 윤년이 아닙니다")
    return year
if __name__ == "__main__":
    is_leap_year()