row = int(input("行数を入力してください: "))
col = int(input("列数を入力してください: "))

for number1 in range(1, row + 1):
    for number2 in range(1, col + 1):
        result = number1 * number2
        print(f"{number1} x {number2} = {result} | ", end=" ")
    print()
