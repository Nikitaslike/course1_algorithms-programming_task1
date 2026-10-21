import math

class Tasks:
    def task1(self):
        #Виведення "Hello, World!" на екран.
        print("Hello, World!")
        
    def task2(self):
        #Розробити програму, яка запитує у користувача його ім'я та вітає його.
        user_name = input("Напишіть ваше ім'я: ")
        print(f"Привіт, {user_name}!")
        
    def task3(self):
        #Введення числа з клавіатури та виведення на екран його подвоєного значення, квадрата та куба.
        number = float(input("Введіть число: "))
        print(f"Подвоєнний: {number * 2}")
        print(f"Квадрат: {number ** 2}")
        print(f"Куб: {number ** 3}")

    def task4(self):
        #Введення двох чисел з клавіатури та виведення на екран їх суми, різниці, добутку та частки.
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))    
        
        print(f"Сума: {num1 + num2}")
        print(f"Різниця: {num1 - num2}")
        print(f"Добуток: {num1 * num2}")
        if num2 == 0:
            print("Ділення на нуль неможливе!")
        else:
            print(f"Частка: {num1 / num2}")

    def task5(self):
        #Введення трьох чисел з клавіатури та виведення на екран середнього за значенням.
        
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
        
        average = (num1 + num2 + num3) / 3
        print(f"Середнє значення: {average}")
        
    def task6(self):
        #Введення радіуса кола з клавіатури та обчислення його площі.
        
        radius = float(input("Введіть радіус кола: "))
        area = 3.14 * radius ** 2
        print(f"Площа кола: {area}")
        area_simplified = radius ** 2
        print(f"Площа кола (спрощено): {area_simplified}π")
        
    def task7(self):
        #Введення довжини та ширини прямокутника з клавіатури та обчислення його площі та периметру.
        
        width = float(input("Введіть ширину прямокутника: "))
        length = float(input("Введіть довжину прямокутника: "))
        area = width * length
        perimeter = 2 * (width + length)
        print(f"Площа прямокутника: {area}")
        print(f"Периметр прямокутника: {perimeter}")

    def task8(self):
        #Виведення на екран парних або непарних (за вибором користувача) чисел від 1 до значення обраного користувачем.
        
        n = int(input("Введіть число: "))
        choice = input("Введіть 'парні' або 'непарні': ")
        if choice == "парні":
            for i in range(2, n + 1, 2):
                print(i)
        elif choice == "непарні":
            for i in range(1, n + 1, 2):
                print(i)
                                
    def task9(self):
        #Виведення на екран таблиці множення на Х (обирається користувачем).
        
        x = int(input("Введіть число: "))
        
        for i in range(1, 11):
            print(f"{x} x {i} = {x * i}")
            
    def task10(self):
        #Введення рядка з клавіатури та виведення на екран його довжини та першої та останньої літер.
        
        string = str(input("Введіть рядок: "))
        print(f"Довжина рядка: {len(string)}")
        print(f"Перша літера: {string[0]}")
        print(f"Остання літера: {string[-1]}")
        
    def task11(self):
        #Написати програму, яка буде приймати від користувача число та перевіряти, 
        # чи є воно парним. Якщо число парне - вивести "Це парне число", якщо непарне - "Це непарне число".
        
        number = int(input("Введіть число: "))
        if number % 2 == 0:
            print("Це парне число")
        else:
            print("Це непарне число")
            
    def task12(self):
        #Написати програму, яка буде створювати список чисел від 1 до 100 
        #та виводити лише ті, які діляться на 3 або 5 без остачі.
        
        for i in range(1, 101):
            if i % 3 == 0 or i % 5 == 0:
                print(i, end=" ")
                
    def task13(self):
        #Написати програму, яка обчислює факторіал числа, яке вводить користувач.
        
        n = int(input("Введіть число: "))
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Факторіал числа {n}: {factorial}")
        
    def task14(self):
        #Написати програму вирішення квадратних рівнянь. Користувач вводить коефіцієнти a, b, c. 
        #бчислити корені квадратного рівняння. Вивести корені або повідомлення, що коренів немає / лише один.
        
        
        num_a = float(input("Введіть коефіцієнт a: "))
        num_b = float(input("Введіть коефіцієнт b: "))
        num_c = float(input("Введіть коефіцієнт c: "))
        
        discriminant = num_b ** 2 - 4 * num_a * num_c
        if discriminant > 0:
            root1 = (-num_b + discriminant ** 0.5) / (2 * num_a)
            root2 = (-num_b - discriminant ** 0.5) / (2 * num_a)
            print(f"Корені рівняння: {root1} та {root2}")
        elif discriminant == 0:
            root = -num_b / (2 * num_a)
            print(f"Рівняння має один корінь: {root}")
        else:
            print("Рівняння не має дійсних коренів.")
            
    def task15(self):
        print("Розв’язання рівняння вигляду |ax + b| = c")
        
        num_a = float(input("Введіть коефіцієнт a: "))
        num_b = float(input("Введіть коефіцієнт b: "))
        num_c = float(input("Введіть число c: "))

        print(f"\nРівняння: |{num_a}x + {num_b}| = {num_c}")
        
        if num_c < 0:
            print("Рівняння не має розв'язків, оскільки модуль не може бути від'ємним.")
        
        elif num_a != 0:
            if num_c == 0:
                x = -num_b / num_a
                print(f"Рівняння має один розв'язок: x = {x}")
            else:
                x1 = (num_c - num_b) / num_a
                x2 = (-num_c - num_b) / num_a
                print(f"Розв'язки рівняння: x1 = {x1}, x2 = {x2}")
        else:
            if abs(num_b) == num_c:
                print("Рівняння має безліч розв'язків (будь-яке x є розв'язком).")
            else:
                print("Рівняння не має розв'язків (ліва частина не дорівнює правій).")

    def task16(self):
        #Користувач вводить десяткове число. Вивести його представлення у двійковій, вісімковій та шістнадцятковій системах числення.
        
        number_10 = int(input("Введіть число: "))
        
        print("Через bin oct hex:")
        print(f"Двійкова: {bin(number_10)}")
        print(f"Вісімкова: {oct(number_10)}")
        print(f"Шістнадцяткова: {hex(number_10)}")
        
        print("Через форматування:")
        print("Двійкова: {:b}".format(number_10))
        print("Вісімкова: {:o}".format(number_10))
        print("Шістнадцяткова: {:x}".format(number_10))
            
    def task17(self):
        #Користувач вводить число >1. Програма визначає, чи є воно простим, 
        #і виводить список усіх дільників, якщо ні.
        
        user_input = int(input("Введіть число більше 1: "))
        if user_input > 1:
            if (user_input % 2 == 0):
                print(f"{user_input} - не просте число")
            else:
                print(f"{user_input} - просте число")
    
    def task18(self):
        #Обчислення НСД і НСК. Для двох введених чисел знайти їх найбільший спільний дільник (НСД) 
        #і найменше спільне кратне (НСК).
        
        user_input1 = int(input("Введіть перше число: "))
        user_input2 = int(input("Введіть друге число: "))

        a, b = user_input1, user_input2
        while b:
            a, b = b, a % b
        nsd = a
        
        if nsd != 0:
            nsk = abs(user_input1 * user_input2) // nsd
        else:
            nsk = None

        print(f"НСД: {nsd}")
        print(f"НСК: {nsk}")
        
    def task19(self):
        #Програма загадує випадкове число від 1 до 100. Користувач намагається вгадати, а програма підказує: більше / менше / вгадано. Обмежити спроби.
        
        user_input = int(input("Введіть число від 1 до 100: "))
        attempts = int(input("Введіть кількість спроб: "))
        import random
        random_number = random.randint(1, 100)
        
        if user_input < 1 or user_input > 100:
            print("Число повинно бути від 1 до 100.")
            return
        if attempts <= 0:
            print("Кількість спроб повинна бути більше 0.")
            return
        
        while attempts > 0:
            if user_input < random_number:
                print("Більше")
            elif user_input > random_number:
                print("Менше")
            else:
                print("Вгадано!")
                break
            attempts -= 1
            if attempts > 0:
                user_input = int(input(f"Спроба не вгадана. Залишилось спроб: {attempts}. Спробуйте ще раз: "))
            else:
                print(f"Спроби закінчилися. Загадане число було: {random_number}")

    def task20(self):
        #Реалізувати меню для конвертації між °C, °F, K з відповідними formулами. Обробити введення та некоректні значення (наприклад, <0K).
        
        try:
            value = float(input("Введіть значення для конвертації: "))
        except ValueError:
            print("Некоректне значення: введіть число.")
            return

        units = ("C", "K", "F")

        mode_from = input("Введіть із чого конвертувати (C, K, F): ").strip().upper()
        if mode_from not in units:
            print("Некоректне значення одиниці вимірювання")
            return

        mode_to = input("Введіть у що конвертувати (C, K, F): ").strip().upper()
        if mode_to not in units:
            print("Некоректне значення одиниці вимірювання")
            return

        if (mode_from == "C" and value < -273.15) or \
        (mode_from == "K" and value < 0) or \
        (mode_from == "F" and value < -459.67):
            print("Некоректне значення: температура нижча за абсолютний нуль!")
            return

        if mode_from == mode_to:
            result = value
        elif mode_from == "C":
            result = value + 273.15 if mode_to == "K" else value * 9/5 + 32
        elif mode_from == "K":
            result = value - 273.15 if mode_to == "C" else (value - 273.15) * 9/5 + 32
        elif mode_from == "F":
            result = (value - 32) * 5/9 if mode_to == "C" else (value - 32) * 5/9 + 273.15

        print(f"Результат: {value}°{mode_from} = {round(result, 2)}°{mode_to}")

    def task21(self):
        #Користувач вводить n. Програма виводить перші n чисел Фібоначчі. 
        #Не використовувати рекурсію.
        recursion_limit = 1000
    
    def task22(self):
        #n студентів беруть k яблук і розподіляють між собою порівну. Решта фруктів залишається в кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику? Програма зчитує числа n і k і друкує на екрані дві відповіді на поставлені вище запитання.
        
        students = int(input("Введіть кількість студентів: "))
        while students <= 0:
            print("Кількість студентів повинна бути більше 0.")
            students = int(input("Введіть кількість студентів: "))
        
        apples = int(input("Введіть кількість яблук: "))
        while apples <= 0:
            print("Кількість яблук повинна бути більше 0.")
            apples = int(input("Введіть кількість яблук: "))

        apples_per_student = apples // students
        remaining_apples = apples % students

        print(f"Кожен студент отримає {apples_per_student} яблук.")
        print(f"У кошику залишиться {remaining_apples} яблук.")


    def task23(self):
        #Класифікація трикутника + площа (Герон). За сторонами a,b,c перевірити існування трикутника, 
        #визначити тип (рівносторонній/рівнобедрений/різносторонній; прямий/тупий/гострий), 
        #обчислити площу за Героном. Потрібно: чіткі повідомлення для кожного випадку.
        
        a = b = c = 0.0
        
        while a + b <= c: 
            a = float(input("Введіть сторону трикутника а: "))
            while a<= 0: 
                print("Сторони трикутника, мають бути більше за 0")
                a = float(input("Введіть сторону трикутника а: "))
            b = float(input("Введіть сторону трикутника b: "))
            while b<= 0: 
                print("Сторони трикутника, мають бути більше за 0: ")
                b = float(input("Введіть сторону трикутника b: "))
            c = float(input("Введіть сторону трикутника c: "))
            while c<= 0: 
                print("Сторони трикутника, мають бути більше за 0")
                c = float(input("Введіть сторону трикутника c: "))

            a, b, c = sorted([a, b, c])
            
            if a + b <= c:
                print(f"Трикутник зі сторонами {a}, {b}, {c}... не створено! Адже умова існування трикутника не виконана;P\nTip: умова існування трикутника a + b > c")
            
            # while not a<=b and b<=c: 
            #     if(a >= b):
            #         a, b = b, a
            #     elif(a > c):
            #         a, c = c, a
            #     elif(b > c):
            #         b, c = c, b
            #     else: 
            #         break 
            
        print(f"Трикутник зі сторонами {a}, {b}, {c} см створено!")
        
        angle_type = ""
        is_sides_equal= ""
        
        if math.isclose(a**2 + b**2, c**2):
            angle_type = "прямокутний"
        elif a**2 + b**2 > c**2:
            angle_type = "гострокутний"
        else:
            angle_type = "тупокутний"
        
        if a == b and b == c:
            is_sides_equal = "рівносторонній"
        elif a == b or b == c:
            is_sides_equal = "рівнобедренний"
        else:
            is_sides_equal = "не рівносторонній і нерівнобедренний"
            
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
        print(f"Тип за сторонами: {is_sides_equal}")
        print(f"Тип за кутами: {angle_type}")
        print(f"Площа трикутника: {area:} см²")
        

#тут використовую ООП:)
def main():    
    
    task = Tasks()
    
    while True:
        print("\nВиберіть завдання (1-23) або введіть 0 для виходу:")
        choice = input("Введіть номер завдання: ")
        if choice == "0" or choice == "exit":
            print("Пока")
            break
        elif choice == "1":
            task.task1()
        elif choice == "2":
            task.task2()
        elif choice == "3":
            task.task3()
        elif choice == "4":
            task.task4()
        elif choice == "5":
            task.task5()
        elif choice == "6":
            task.task6()
        elif choice == "7":
            task.task7()
        elif choice == "8":
            task.task8()
        elif choice == "9":
            task.task9()
        elif choice == "10":
            task.task10()
        elif choice == "11":
            task.task11()
        elif choice == "12":
            task.task12()
        elif choice == "13":
            task.task13()
        elif choice == "14":
            task.task14()
        elif choice == "15":
            task.task15()
        elif choice == "16":
            task.task16()
        elif choice == "17":
            task.task17()
        elif choice == "18":
            task.task18()
        elif choice == "19":
            task.task19()
        elif choice == "20":
            task.task20()
        elif choice == "21":
            task.task21()
        elif choice == "22":
            task.task22()
        elif choice == "23":
            task.task23()
        elif choice == "67": 
            print(r"""
              ⢀⠤⣂⣤⣬⣭⣭⣭⣔⡠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠔⣵⣾⣿⣿⣿⢿⣿⣿⣿⣿⣎⢂⠀⢲⣤⣤⣤⣤⣀⣒⣒⣒⣒⣂⡠⠤⠤⣄
            ⠐⣾⣿⣿⣿⡏⣾⡿⢎⣛⣫⣭⣴⣾⠆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼
            ⡇⣿⣿⣿⣿⣟⡿⢀⣐⣻⣛⡩⢁⠀⠀⣘⣛⣛⡛⠿⠿⠿⢿⣿⣿⣿⣿⣿⢟⣾
            ⡇⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣶⡕⠄⠉⠛⠛⠛⠛⡻⣣⣾⣿⣿⣿⢟⣵⣿⠛
            ⠃⣿⣿⣿⣿⣿⢋⣥⠭⡻⣿⣿⣿⣿⡌⡄⠀⠀⠀⡐⣼⣿⣿⣿⡿⣣⣾⠏⠀⠀
            ⠨⢻⣿⣿⣿⣧⢻⠁⠀⠘⢸⣿⣿⣿⡇⣿⠀⠀⠌⣼⣿⣿⣿⡿⢱⣿⠃⠀⠀⠀
            ⠀⢦⢻⣿⣿⣿⣦⣐⣀⣊⣼⣿⣿⡿⢱⡿⠀⠰⣸⣿⣿⣿⣿⢣⣿⠃⠀⠀⠀⠀
            ⠀⠀⠣⣙⠿⣿⣿⣿⣿⣿⣿⠿⢛⣵⡿⠃⢀⢃⣿⣿⣿⣿⡟⣾⡇⠀⠀⠀⠀⠀
            ⠀⠀⠀⠈⠛⠶⣮⣭⣭⣴⣶⡿⠿⠋⠀⠀⢨⣘⣿⡻⠿⠿⢇⣿⠀⠀⠀⠀⠀⠀
            ⠀⠀⢀⠔⠒⠂⠠⠤⠭⡀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠻⠃⠀⠀⠀⠀⠀⠀
            ⢀⠆⠁⠀⡄⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠁⠀⠀⠒⢤⡀⠀⠀
            ⠣⠤⢤⠞⠂⠀⣀⠰⠃⠀⠘⣆⢀⣀⠀⠀⠀⠀⢀⠎⠀⢠⡀⠀⠀⠀⢀⠀⠙⡀
            ⠀⠀⢸⠀⠈⠭⡀⢈⣡⠔⢶⠁⣹⢩⠃⠀⢀⠀⢸⠀⠀⠀⣑⣠⣤⠀⠙⡦⣀⠜
            ⠀⠀⠀⠣⠀⢂⠞⠱⠴⣈⡸⠰⢇⠘⠀⠰⡭⠷⢝⡤⣂⣄⠒⢤⡐⠀⠀⡇⠀⠀
            ⠀⠀⠀⠀⠱⠄⣀⢜⢁⡠⠥⠊⠀⠀⠀⠀⠡⡘⡄⠐⡂⠘⢌⡀⠉⠂⡸⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠄⠹⢅⣀⠹⠒⠊⠀⠀⠀
            """)
            
        else: 
            print("н..А...пиШИ НорМ....АЛЬНЕ... ЧисЛо зАВ..даННя!!!!.....\nПерепрошую, не хотів Вас налякати:D")
        
        
if __name__ == "__main__":
    main()