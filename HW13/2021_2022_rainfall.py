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
def sum_annual(rainfalls,years):
    dataset = {}
    for y in range(2001,2023):
        dataset[y] = sumifs(rainfalls, years, [y])
    return dataset
def main():
    weather_filename = "weather(146)_2001-2022.csv"
    rainfalls = read_weather_col(weather_filename, 9, as_type=float)
    years = read_weather_col(weather_filename, 0, as_type=int)
    rainfall_2021 = sumifs(rainfalls, years,[2021])
    rainfall_2022 = sumifs(rainfalls,years, [2022])
    #print(f"2021년총강수량은 {rainfall_2021:.1f} mm입니다")
   # print(f"2021년총강수량은 {rainfall_2022:.1f} mm입니다")
    for y in range(2001,2022):
        rainfall_y = sumifs(rainfalls, years, [y])
        print(f"{y}년 총강수량은 {rainfall_y:.1f} mm입니다")
    rainfall_annual = sum_annual(rainfalls,years)
    #print(rainfall_annual[2005])
if __name__ == '__main__':
    main()
