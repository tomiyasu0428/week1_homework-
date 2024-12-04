info = input("データを入力してください(スペース区切り) > ")
info = list(map(int, info.split()))

# 合計値の関数


def date_sum(info):
    info_sum = 0
    for i in info:
        info_sum += i
    return info_sum


print(f"合計値: {date_sum(info)}")

# 最大値の関数


def data_max(info):
    number_max = info[0]
    for j in info:
        if j >= number_max:
            number_max = j
    return number_max


print(f"最大値: {data_max(info)}")

# 最小値の関数


def date_min(info):
    number_min = info[0]
    for k in info:
        if k <= number_min:
            number_min = k
    return number_min


print(f"最小値: {date_min(info)}")

# 平均値の関数


def date_ava(info):
    num_sum = info[0]
    for num in info:
        num_sum += num

    num_num = len(info)
    num_ava = num_sum / num_num

    return num_ava


print(f"平均値: {int(date_ava(info))}")


# 実行結果
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6
