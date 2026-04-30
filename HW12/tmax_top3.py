def read_tmax(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def get_top3(list_values):\
    return sorted(list_values)[-3:]

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    tmax = read_tmax(weather_filename)
    tmax_event= get_top3(tmax)
    print(f"가장 더운날 TOP3는 {tmax_event}입니다")
if __name__ == "__main__":
    main()