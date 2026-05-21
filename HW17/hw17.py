from lec15 import default_value


def str2int(text: str):
    try:
        return int(text)
    except ValueError:
        return None
def main():
    values =[]
    while True:
        x = input("x=>?")
        x_value = str2int(x)
        if x_value == -1:
            break
        if x_value is not None:
            if x_value > 0 and type(x_value) == int:
                values.append(x_value)
    print(f"입력된 값: {values}")
    print(f"입력된 값의 갯수: {len(values)}")
    print(f"입력된 값의 평균: {sum(values)/len(values)}")

if __name__ == "__main__":
    main()