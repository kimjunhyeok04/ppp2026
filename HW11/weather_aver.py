def read_tavgs(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[3]))
    return dataset
def main():
    weather_filename = "weather(146)_2022-2022.csv"
    tavgs = read_tavgs(weather_filename)
    print(f"연 평균 온도는 {sum(tavgs) / len(tavgs)}")
if __name__ == "__main__":
    main()