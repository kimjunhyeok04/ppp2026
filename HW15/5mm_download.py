import requests
def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            if len(tokens) > 3:
                dataset.append(float(tokens[9]))
    return dataset
def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5:
            count_5mm += 1
    return count_5mm
def main():
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    filename = "weather_2023.csv"
    response = requests.get(url)
    open(filename, "w").write(response.text)
    rainfall = read_rainfall(filename)
    days_over_5mm = get_days_over_5mm(rainfall)
    f = open("result_file.txt", "w", encoding="utf-8")
    f.write(f"5mm 이상인 총 강우일수는 {days_over_5mm}일입니다")
    f.close()
if __name__ == "__main__":
    main()
