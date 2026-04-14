def main():
    numbers = []
    with open("numbers2.txt") as f:
        for line in f:
            if line.strip():
                numbers.append(int(line))
    total = len(numbers)
    print(f"총 숫자의 개수는 {total}입니다")
    aver = sum(numbers) / total
    print(f"평균값은 {aver}입니다")
    maximum = max(numbers)
    print(f"최댓값은 {maximum}입니다")
    minimum = min(numbers)
    print(f"최솟값은 {minimum}입니다")
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 1:
        med = numbers[mid]
    else:
        med = (numbers[mid - 1] + numbers[mid]) / 2
    print(f"중앙값은 {med}입니다")
if __name__ == "__main__":
    main()