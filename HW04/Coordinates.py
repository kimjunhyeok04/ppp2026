X1 = input("X1 좌표를 입력해주세요")
X1 = int(X1)
Y1 = input("Y1 좌표를 입력해주세요")
Y1 = int(Y1)
if X1 < 0 and Y1 > 0 :
    print(f"좌표는 {X1},{Y1}이며 1사분면에 위치합니다")
elif X1 > 0 and Y1 > 0 :
    print(f"좌표는 {X1},{Y1}이며 2사분면에 위치합니다")
elif X1 < 0 and Y1 < 0 :
    print(f"좌표는 {X1},{Y1}이며 3사분면에 위치합니다")
elif X1 > 0 and Y1 < 0 :
    print(f"좌표는 {X1},{Y1}이며 4사분면에 위치합니다")
else :
    print(f"좌표는 {X1},{Y1}이며 어느 사분면에도 속하지 않습니다")