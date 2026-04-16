def main():
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
    eat_dict = {"한라봉": 100, "딸기": 200, "바나나": 500}
    total_cal = 0
    for fruit in cal_dict:
        total_cal += cal_dict[fruit] * eat_dict[fruit]
    print(f"총 칼로리는 {total_cal}kcal입니다")
if __name__=="__main__":
    main()
