
def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset
def get_max_rainfall_event(rainfall):
    datasets = []
    rainfall_event = None
    for r in rainfall:
        if r >0:
            if rainfall_event != None:
                rainfall_event.append(r)
            else:
                rainfall_event = [r]
        else:
            if rainfall_event != None:
                datasets.append(rainfall_event)
            rainfall_event = None
    if rainfall_event != None:
        datasets.append(rainfall_event)
    print(datasets)
    print("7확인")
    print(max([len(x) for x in datasets]))
    return max([sum(x) for x in datasets])
def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_rainfall(weather_filename)
    max_rainfall_event = get_max_rainfall_event(rainfall)
    print(f"최대 강수량은 {max_rainfall_event}입니다")
if __name__ == "__main__":
    main()