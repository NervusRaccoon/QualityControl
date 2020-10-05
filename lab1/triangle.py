def check(list):
    if len(list) == 3:
        try:
            a, b, c = float(list[0]), float(list[1]), float(list[2])
        except ValueError:
            result = 'Неизвестная ошибка'
        else:
            if a <= 0 or b <= 0 or c <= 0:
                result = 'Неизвестная ошибка'
            elif a + b <= c or a + c <= b or b + c <= a:
                result = 'Не треугольник'
            elif a == b == c:
                result = 'Равносторонний треугольник'
            elif a == b or b == c or a == c:
                result = 'Равнобедренный треугольник'
            else:
                result = 'Обычный треугольник'
    else:
        result = 'Неизвестная ошибка'

    return result

def main():
    args = input()
    args = args.split(' ')
    print(check(args))

if __name__ == '__main__':
    main()
