import requests
def read_tavgs(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            if len(tokens) > 3:
                dataset.append(float(tokens[2]))
    return dataset
def main():
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    filename = "weather_2023.csv"
    response = requests.get(url)
    open(filename, "w").write(response.text)
    tavgs = read_tavgs(filename)
    f = open("result_file.txt", "w",encoding="utf-8")
    f.write(f"연 평균 온도는 {sum(tavgs) / len(tavgs):.2f}°C")
    f.close()

if __name__ == "__main__":
    main()