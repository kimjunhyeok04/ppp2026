import math
r = input("반지름을 입력해주세요")
r = int(r)
circumference = 2 * math.pi * r
suclespace = math.pow(r,2) * 3.141592
print("원의 둘레는 {:.1f}입니다".format(circumference))
print("원의 면적은 {:.2f}입니다".format(suclespace))