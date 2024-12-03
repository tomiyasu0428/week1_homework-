import random

saikoro_n = int(input("サイコロの面の数は?: "))
saikoro_m = int(input("何回ふりますか？: "))

result = []

play_time = 0
for play_time in range(0, saikoro_m):
    saikoro_number = random.randint(1, saikoro_n)
    result.append(saikoro_number)
    play_time += 1

print(result)
