def toggle_ch(alphabet):
  if ord(alphabet) >= 65 and ord(alphabet) <= 90:
      return chr(ord(alphabet) + 32)
  elif ord(alphabet) >= 97 and ord(alphabet) <= 122:
      return chr(ord(alphabet) - 32)
  else:
      return alphabet
def toggle_text(text):
    result = ""
    for c in text:
        result += toggle_ch(c)
    return result
def main():
    alphabet = input("암호화 하고 싶은 단어를 말해주세요")
    print(toggle_text(f"변환한 값은 {alphabet}입니다."))
if __name__ == "__main__":
    main()
#input을 사용해서 해보았습니다!