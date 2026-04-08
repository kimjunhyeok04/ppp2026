def main():
    cal_orange = 50
    cal_sb = 34
    cal_banana = 77
    cal_list = [50, 34, 77]
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
    total_cal = cal_list[0] + cal_list[1] + cal_list[2]
    eat_orange = 100
    eat_sb = 200
    eat_banana = 500
    eat_list = [100, 200, 500]
    total_cal_list = (cal_list[0] * eat_list[0] + cal_list[1] * eat_list[1] + cal_list[2] * eat_list[2])
    for i in range(3): total_cal_list += cal_list[i] * eat_list[i]
    print(total_cal_list)
if __name__=="__main__":
    main()
