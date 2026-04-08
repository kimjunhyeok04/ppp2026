def sum_m():
    n = int(input("숫자를 입력해주세요"))
    total = 0
    for i in range(n+1):
        total += i
    return total
if __name__=="__main__":
    print(sum_m())
