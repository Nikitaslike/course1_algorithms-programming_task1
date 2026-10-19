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
        print(f"Двійкове представлення: {number_10:b}")
        print(f"Вісімкове представлення: {number_10:o}")
        print(f"Шістнадцяткове представлення: {number_10:X}")

#тут використовую ООП:)
def main():
    task = Tasks()
    choice = input("Введіть номер завдання: ")
    if(choice == "1"):
        task.task1()
    elif(choice == "2"):
        task.task2()
    elif(choice == "3"):
        task.task3()
    elif(choice == "4"):
        task.task4()
    elif(choice == "5"):
        task.task5()
    elif(choice == "6"):
        task.task6()
    elif(choice == "7"):
        task.task7()
    elif(choice == "8"):
        task.task8()
    elif(choice == "9"):
        task.task9()
    elif(choice == "10"):
        task.task10()
    elif(choice == "11"):
        task.task11()
    elif(choice == "12"):
        task.task12()
    elif(choice == "13"):
        task.task13()
    elif(choice == "14"):
        task.task14()
    elif(choice == "15"):
        task.task15()
    elif(choice == "16"):
        task.task16()   
if __name__ == "__main__":
    main()