def read_weather_col(filename, col_index, as_type=float):
    dataset = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if len(tokens) <= col_index or tokens[col_index] == "":
                continue
            try:
                dataset.append(as_type(tokens[col_index]))
            except ValueError:
                continue
    return dataset

def sumifs(rainfalls, months, selected_months):
    total_value = 0.0
    for i in range(min(len(rainfalls), len(months))):
        r = rainfalls[i]
        m = months[i]
        if m in selected_months:
            total_value += r
    return total_value

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfalls = read_weather_col(weather_filename, 9, as_type=float)
    months = read_weather_col(weather_filename, 1, as_type=int)
    summer_rainfall = sumifs(rainfalls, months, [6, 7, 8])
    print(rainfalls)
    print(f"여름철 강수량은 {summer_rainfall:.1f} mm입니다")

if __name__ == '__main__':
    main()
