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
def get_all_rainfall(rainfall):
    all_rainfall = 0.0
    for r in (rainfall):
        all_rainfall += r
    return all_rainfall
def main():
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    filename = "weather_2023.csv"
    response = requests.get(url)
    open(filename, "w").write(response.text)
    rainfall = read_rainfall(filename)
    all_rainfall = get_all_rainfall(rainfall)
    f = open("result_file.txt", "w", encoding="utf-8")
    f.write(f"총 강수량은 {all_rainfall:.2f}mm 입니다")
    f.close()
if __name__ == "__main__":
    main()
