number1 = int(input("行数を入力してください: "))
number2 = int(input("列数を入力してください: "))

for number1 in range(1, number1 + 1):
    for number2 in range(1, number2 + 1):
        result = number1 * number2
        print(result, end=" ")
    print()
