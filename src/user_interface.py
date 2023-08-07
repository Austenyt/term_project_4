from user_print import print_operations, print_welcome_user_1, print_welcome_user_2
from user_print import print_result_search
from headhunter import HeadHunter
from superjob import SuperJob
from json_job_file import JSONJobFile
from vacancy import Vacancy


def run_user_interface():
    """Функция для взаимодействия с пользователем в консоли."""
    global res
    global vacancies

    flag_1 = True

    hh = HeadHunter
    sj = SuperJob
    list_platforms = [hh, sj]

    print_welcome_user_1()

    # Блок получения информации о вакансиях с выбранной платформы в России
    while flag_1:
        print("Выберите платформу, с которой хотите получить вакансии: ")
        print_welcome_user_2()
        user_input_pl = input("Введите одну из предложенных цифр: ")
        if user_input_pl in ["1", "2"]:
            platform = list_platforms[int(user_input_pl) - 1]
            print(f"Выбран сайт {platform()}\n")

            while True:
                print("Выберите операцию, связанную с выводом информации о вакансиях: ")
                print_operations()
                choice = input("Введите одну из предложенных цифр: ")

                if choice == "1":
                    search_query = input("Введите поисковый запрос: ")
                    res = platform().get_vacancies_api(search_query)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "2":
                    search_query = input("Введите поисковый запрос: ")
                    n_salary = int(input("Сколько получить вакансий по зарплате? "))
                    if 0 < int(n_salary) < 100:
                        res = platform().get_vacancies_api(search_query)
                    elif int(n_salary) < 0:
                        res = platform().get_vacancies_api(search_query)
                    else:
                        res = platform().get_vacancies_api(search_query)
                    print(print_result_search(platform, res, "Зарплата"))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "3":
                    print("Выберите регион из списка\n1. Москва\n2. Санкт-Петербург")
                    region = input("Введите номер региона: ")
                    res = platform().get_region_vacancies(region)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "4":
                    keywords = input("Получить вакансии, по ключевому слову в описании: ")
                    n = input("Количество для вывода: ")
                    res = platform().get_region_vacancies(keywords)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "0":
                    break

                else:
                    print("\nВЫБЕРИ ЗАПРОС ВЕРНО!\n")
                    continue

            # Блок сохранения информации о вакансиях в файл
            filename = "data_vacancies.json"
            js_file = JSONJobFile(filename)  # JSON
            file_path = js_file.add_vacancy(res)

        elif user_input_pl == "0":
            flag_1 = False
            print("До свидания!")
        else:
            print("Платформа выбрана неверно!")


if __name__ == "__main__":
    run_user_interface()
