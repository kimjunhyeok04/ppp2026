def get_range_list():
    num = int(input("리스트로 만들 n번째 숫자를 입력해주세요"))
    result = []
    for i in range(1,num+1):
        result = result + [i]
    return result
if __name__ == "__main__":
    print(get_range_list())