total = 0
for n in range(1,251):
    if n % 2 ==0:
        total += n
print(total)

print(sum([ X for X in range(1,251) if X % 2 ==0]))