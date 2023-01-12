
def get_value():
    print("Привет! Добро пожаловать в ^особенный^ калькулятор для работы с рациональными числами.")
    kind_operation = input("Для работы с комплексными числами введите - 1")
   
    while True:
        inp = input("Выберите операцию. Увага! -=Пожалуйста, отделяйте цифры от знака операции пробелом=- ")
        try_act = inp
        data = try_act.split()

        if len(data) == 3:
            if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
                print("Спаси....спасибо!")
                break

        print("Ничего не понятно, но очень интресно")

    return inp, kind_operation

def output(result):
    try:
        if result.is_integer():
            print(f"Результат--", int(result))
        elif isinstance(result, float):
            print(f"Результат--", result)
        else: print(result)
    except:
        print(result)
