def calculator():
    print("簡単な計算機")
    num1 = float(input("最初の数字を入力してください: "))
    operator = input("演算子を入力してください (+, -, *, /): ")
    num2 = float(input("次の数字を入力してください: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("ゼロで割ることはできません。")
            return
        result = num1 / num2
    else:
        print("無効な演算子です。")
        return
    
    print(f"結果: {result}")

if __name__ == "__main__":
    calculator()