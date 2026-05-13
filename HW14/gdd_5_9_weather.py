def read_dates(filename):
    dates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            year = tokens[0]
            month = tokens[1]
            day = tokens[2]
            date = year + "-" + month + "-" + day
            dates.append(date)
    return dates
def read_weather_col(weather_filename, col_index):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            value = float(tokens[col_index])
            values.append(value)
    return values

def gdd_season(dates, tavg):
    gdd_values = 0
    for i in range(len(dates)):
        date = dates[i]
        month = int(date.split("-")[1])
        t = tavg[i]
        if month in [5,6,7,8,9]:
            if t >= 5:
                gdd_values += t - 5
    return gdd_values
def main():
    weather_filename = "weather(146)_2022-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)
    gdd_value = gdd_season(dates, tavg)
    print(f"GDD는 {gdd_value:.1f}입니다")


if __name__ == '__main__':
    main()