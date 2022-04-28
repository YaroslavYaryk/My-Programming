def one():
    input_data = int(input("Ведіть дані: "))

    services = {
        101: "МНС",
        102: "Поліція",
        103: "Швидка",
        104: "Газова служба",
        112: "Центр громадської безпеки",
    }

    result = services.get(input_data)

    print(result) if result else print("Перевірте правильність введення даних")


def two():

    m, n, k = map(int, input("Введіть m n k: ").split())

    print("Так") if not k % m or not k % n else print("Ні")


def three():

    arr = []

    while True:
        res = int(input("Введіть кількість очок: "))
        if not res:
            break
        arr.append(res)

    print(f"Переміг учасник, що набрав { max(arr)} голосів")


def four():

    arr = []

    while True:
        res = int(input("Введіть кількість очок: "))
        if not res:
            break
        arr.append(res)

    print(f"Гравець набрав { sum(arr)} голосів")


def five():
    current_year = int(input("Введіть поточний рік: "))
    end_year = int(input("Введіть рік закінчення депозиту: "))
    start_installment = int(input("Введіть суму початкового вкладу: "))
    deposit_percentage = int(input("Введіть відсоток депозиту: ")) / 100

    result = start_installment * (1 + deposit_percentage) ** (end_year - current_year)

    print(
        f"Сума депозиту за {end_year - current_year} років є рівною {round(result, 2)} галеонів"
    )
