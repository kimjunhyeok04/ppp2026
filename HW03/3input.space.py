upper = input("윗 변의 길이를 알려주세요.")
upper = int(upper)
lower = input("밑 변의 길이를 알려주세요")
lower = int(lower)
height = input("높이를 알려주세요.")
height = int(height)
trapezoidal = (upper + lower) * height / 2
print(f"사다리꼴에 면적은 {trapezoidal}입니다.")