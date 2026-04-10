def average():
    num = input("숫자를 한 개씩 띄어서 입력해주세요: ")
    numbers = num.split()
    sum_1 = 0
    for i in range(len(numbers)):
        sum_1 += int(numbers[i])
    aver = sum_1 / len(numbers)
    print(aver)
    return aver
if __name__ == "__main__":
    average()