def add(left_operand, right_operand): return left_operand + right_operand
def sub(left_operand, right_operand): return left_operand - right_operand
def mul(left_operand, right_operand): return left_operand * right_operand
def div(left_operand, right_operand):
    if right_operand == 0:
        raise ZeroDivisionError
    return left_operand // right_operand

OPERATIONS = {'+': add, '-': sub, '*': mul, '/': div}

def parse_integer(text):
    try:
        return int(text)
    except ValueError:
        return None

def main():
    tokens = []
    while True:
        user_input = input("> ").strip()
        if user_input == '=':
            break
        if user_input:
            tokens.append(user_input)

    left_operand = parse_integer(tokens[0]) if tokens else None
    if left_operand is None:
        print("Ошибка ввода: первое значение не число")
        return

    index = 1
    while index < len(tokens):
        operator = tokens[index]
        if operator not in OPERATIONS:
            print(f"Ошибка ввода: '{operator}' не оператор")
            return
        # ловит ситуацию если выражение заканчивается на операторе
        if index + 1 >= len(tokens):
            print("Ошибка ввода: нет числа после оператора")
            return

        right_operand = parse_integer(tokens[index + 1])
        if right_operand is None:
            print(f"Ошибка ввода: '{tokens[index + 1]}' не число")
            return

        try:
            left_operand = OPERATIONS[operator](left_operand, right_operand)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
            return
        index += 2

    print("Результат:", left_operand)

main()

