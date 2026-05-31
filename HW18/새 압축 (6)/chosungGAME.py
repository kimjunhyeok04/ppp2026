import random
import re
BASE_CODE, CHOSUNG = 44032, 588
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
def get_chosung(text):
    result = ""
    for char in text:
        if '가' <= char <= '힣':
            char_code = ord(char) - BASE_CODE
            char1 = char_code // CHOSUNG
            result += CHOSUNG_LIST[char1]
        else:
            result += char
    return result
def main():
    words = ["사과", "바나나", "컴퓨터", "프로그래밍", "인공지능", "학교", "자동차"]
    answer = random.choice(words)
    hint = get_chosung(answer)
    print("초성 퀴즈!")
    print("초성:", hint)
    user_input = input("정답을 맞춰보세요: ")
    if user_input == answer:
        print("정답입니다! 🎉")
    else:
        print("틀렸습니다 😢 정답은:", answer)
if __name__ == "__main__":
    main()
