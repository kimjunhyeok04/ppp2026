def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset
def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5:
            count_5mm += 1
    return count_5mm
def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_rainfall(weather_filename)
    days_over_5mm = get_days_over_5mm(rainfall)
    print(f"5mm 이상인 총 강우일수는 {days_over_5mm}일입니다")
if __name__ == "__main__":
    main()
