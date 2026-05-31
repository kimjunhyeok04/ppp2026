def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""
    for c in text:
        if 65 <= ord(c) <= 90:
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        elif 97 <= ord(c) <= 122:
            result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result
def main():
    text = input("문장을 입력하세요: ")
    print(caesar_encode(text))
if __name__ == "__main__":
    main()
#65또는 97을 빼주어 A일 경우 영으로 만들어서 A-z가 0~25로 만들고 시프트 3을 해서
#더 해주어 카이사르 코드를 만들고 초과되는 값을 정정하려 %26을 함