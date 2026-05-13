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


def get_max_diff(dates, tmax, tmin):
    max_diff = 0
    max_diff_date = None
    for i in range(len(dates)):
        diff = tmax[i] - tmin[i]
        if diff > max_diff:
            max_diff = diff
            max_diff_date = dates[i]
    return max_diff, max_diff_date

def main():
    weather_filename = "weather(146)_2022-2022.csv"

    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    temp_diff, date = get_max_diff(dates, tmax, tmin)
    print(f"일교차가 가장 큰 날:{date}")
    print(f"일교차가 가장 큰 날의 일교차는:{temp_diff:.1f}도")

if __name__ == '__main__':
    main()