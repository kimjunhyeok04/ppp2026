mart = {"우유": 2800, "계란" : 300, "빵": 1200, "물" : 1700}
cart = {"우유": 2, "계란" : 3 , "빵": 1, "물" : 5}
total_cash = 0
for key,val in cart.items():
    total_cash += val * mart[key]
print(f"총 가격은{total_cash:,}원입니다")