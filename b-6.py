import random

saikoro_N = int(input("サイコロの面の数は?: "))
saikoro_M = int(input("何回ふりますか？: "))

result = []

play_time = 1
while play_time <= saikoro_M:
    saikoro_number = random.randint(1, saikoro_N)
    result.append(saikoro_number)
    play_time += 1

print(result)
