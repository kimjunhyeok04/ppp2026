def average():
    num = (1,3,4,5,6)
    sum_1 = 0
    for i in range(len(num)):
        sum_1 += num[i]
    aver = sum_1 / len(num)
    print(aver)
    return aver
if __name__ == "__main__":
    average()