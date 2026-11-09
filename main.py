from probability_tests import *
def console_interface():
    # для тестов
    # 561 — Число Кармайкла
    # 1000000007 — простое число
    while True:
        print("\nВероятностные тесты на простоту\n")
        user_input_a = input("Введите число 'N', которое хотите проверить на простоту: ").strip()
        user_input_p = input("Введите число попыток 's': ").strip()
        try:
            N = abs(int(user_input_a))
            s = abs(int(user_input_p))
        except ValueError:
            print("\nВводите только целые числа.\n")
            continue

        try:
            if N == 1 or N == 2:
                print("1 - не простое, 2 - простое")
                continue
            print("Результаты проверок:")
            print(f"\nЧисло N = {N}:")
            print(f" Тест Ферма:{fermat_primality_test(N, s)}")
            print(f" Тест Соловея-Штрассена:{solovay_strassen_test(N, s)}")
            print(f" Тест Миллера-Рабина:{miller_rabin_test(N, s)}")
        except ValueError as e:
            print(f"{e}\n")
            continue

if __name__ == "__main__":
    console_interface()