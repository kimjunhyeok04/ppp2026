cal_dict = {"한라봉": 50, "딸기" : 34, "바나나": 77}
eat_dict = {"한라봉": 100, "딸기" : 200, "바나나": 500}
total_cal = 0
for key, val in eat_dict.items():
    total_cal += val * cal_dict[key]
print(f"총{total_cal:,}칼로리입니다.")