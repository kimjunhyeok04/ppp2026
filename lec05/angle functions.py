import math
for i in range(0, 11):
    rad = math.radians(i)
    s = math.sin(rad)
    c = math.cos(rad)
    t = math.tan(rad)
    print(f"{i}도 | 라디안: {rad:.4f} | sin: {s:.4f} | cos: {c:.4f} | tan: {t:.4f}")