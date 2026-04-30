def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset
def get_rain_event_days(rainfall):
    dataset_rainfall = []
    for r in rainfall:
        if r >0:
            dataset_rainfall.append(1)
        else: # r == 0:
            dataset_rainfall.append(0)
    dataset_rainfall_event = []
    for i in range(len(dataset_rainfall)):
        r = dataset_rainfall[i] # 0 or 1
        if r == 0:
            dataset_rainfall_event.append(0)
        else:
            if i == 0 :
                dataset_rainfall_event.append(1)
            else:
                dataset_rainfall_event.append(dataset_rainfall_event[i-1]+1)
    print(dataset_rainfall_event)
    return max(dataset_rainfall_event)
def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_rainfall(weather_filename)
    max_rainy_days = get_rain_event_days(rainfall)
    print(f"최장 연속 강우일 수 는 {max_rainy_days}일입니다")
if __name__ == "__main__":
    main()