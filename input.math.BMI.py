weight = input("몸무게를 입력해주세요")
weight = int(weight)
height = input("키를 입력해주세요")
height = int(height)
height_1 = height / 100
import math
BMI = weight / (math.pow(height_1,2))
print(f"당신의 BMI는 {BMI}입니다 ")