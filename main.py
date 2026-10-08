class Tasks:
    def helloWorld1(self):
        #Виведення "Hello, World!" на екран.
        print("Hello, World!")
        
    def helloUser2(self):
        #Розробити програму, яка запитує у користувача його ім'я та вітає його.
        user_name = input("Напишіть ваше ім'я: ")
        print(f"Привіт, {user_name}!")
        
    def numberCalculator3(self):
        #Введення числа з клавіатури та виведення на екран його подвоєного значення, квадрата та куба.
        number = float(input("Введіть число: "))
        print("Подвоєнний: ", number * 2)
        print("Квадрат: ", number ** 2)
        print("Куб: ", number ** 3)
        
    def numberCalculator4(self):
        #Введення двох чисел з клавіатури та виведення на екран їх суми, різниці, добутку та частки.
        num1 = float(input("Введіть пероше число: "))
        num2 = float(input("Введіть друге число: "))    
        
        print("Сума: ", num1 + num2)
        print("Різниця: ", num1 - num2)
        print("Добуток: ", num1 * num2)
        if num2 == 0:
            print("Ділення на нуль неможливе!")
        else:
            print("Частка: ", num1 / num2)
            

#тут використовую ООП:)
def main():
    task = Tasks()
    task.helloWorld1()
    task.helloUser2()
    task.numberCalculator3()
    task.numberCalculator4()

if __name__ == "__main__":
    main()