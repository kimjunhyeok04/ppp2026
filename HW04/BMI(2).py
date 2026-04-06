import math
weight = input("몸무게를 입력해주세요")
weight = int(weight)
height = input("키를 입력해주세요")
height = int(height)
height_1 = height / 100
BMI = weight / (math.pow(height_1,2))
if 23 <= BMI <= 24.9 :
    print(f"당신의 BMI지수는 {BMI}이고 비만 전단계입니다")
elif 25 <= BMI <= 29.9 :
    print(f"당신의 BMI지수는 {BMI}이고 비만 1단계입니다")
elif 30 <= BMI <= 34.9 :
    print(f"당신의 BMI지수는 {BMI}이고 비만 2단계입니다")
elif 35 <= BMI :
    print(f"당신의 BMI지수는 {BMI}이고 비만 3단계입니다")
else :
    print(f"당신의 BMI지수는 {BMI}이고 정상입니다")