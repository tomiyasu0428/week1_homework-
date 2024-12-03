def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    temp_sum = 0
    for temp in weather_information:
        temp_sum += temp["temperature"]

    temp_ava = temp_sum / len(weather_information)
    print(temp_ava)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    osaka_stations = []
    for sta in weather_information:
        if sta["prefecture"] == "大阪府":
            osaka_stations.append(sta["station"])

    print(", ".join(osaka_stations))

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    fuku_tempsum = 0
    fuku_count = 0
    for temp_fukuoka in weather_information:
        if temp_fukuoka["prefecture"] == "福岡県":
            fuku_tempsum += temp_fukuoka["temperature"]
            fuku_count += 1

    fuku_temp_ava = fuku_tempsum / fuku_count
    print(fuku_temp_ava)


if __name__ == "__main__":
    main()
