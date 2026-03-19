print("1.화씨->섭씨, 2.섭씨->화씨, 3.피트(ft)->cm, 4.cm->피트(ft)중 어떤걸로 변환할지 숫자를 선택하시오")
choice = input("무엇을 변환할지 번호를 선택하시오")
choice = int(choice)
if choice == 1:
    temp_c = float(input("섭씨 온도를 입력하세요"))
    temp_c = int(temp_c)
    temp_f = (temp_c * 1.8) + 32
    print("{:.1f}F입니다".format(temp_f))
elif choice == 2:
    temp_f = float(input("화씨 온도를 입력하시오."))
    temp_f = int(temp_f)
    temp_c = (temp_f - 32) / 1.8
    print("{:.1f}C입니다".format(temp_c))
elif choice == 3:
    height_ft = float(input("피트길이를 입력하시오."))
    height_ft = int(height_ft)
    height_cm = height_ft *30.28
    print("{:.1f}CM입니다".format(height_cm))
elif choice == 1:
    height_cm = float(input("피트길이를 입력하시오."))
    height_cm = int(height_cm)
    height_ft = height_cm * 30.28
    print("{:.1f}FT입니다".format(height_ft))
else :
    print("선택하신 번호는 잘 못 되었습니다")
