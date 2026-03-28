X1 = input("X1 좌표를 입력해주세요")
X1 = int(X1)
Y1 = input("Y1 좌표를 입력해주세요")
Y1 = int(Y1)
X2 = input("X2 좌표를 입력해주세요")
X2 = int(X2)
Y2 = input("Y2 좌표를 입력해주세요")
Y2 = int(Y2)
import math
distance =math.sqrt((math.pow(abs(X1 -X2),2)) + (math.pow(abs(Y1 - Y2), 2)))
print(f"두 지점 사이의 거리는 {distance}입니다")
if(distance <= 1):
    print("두점이 너무 가깝습니다")
elif(distance > 10):
    print("두점이 너무 멀리 있습니다")
else:
    print("적당하네요")

