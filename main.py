from src.hh_api import HeadHunterAPI
from src.json_storage import JSONStorage


def interact_with_user():
    api = HeadHunterAPI('https://api.hh.ru/vacancies')
    storage = JSONStorage("vacancies.json")

    query = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")
    api.connect()
    vacancies = api.get_vacancies(query)

    count = int(input("Введите количество вакансий для отображения: "))
    top_n_vacancies = sorted(vacancies, reverse=True)[:count]
    print(f"Топ {count} вакансий по зарплате:")
    for i, vacancy in enumerate(top_n_vacancies, start=1):
        print(f"{i}. {vacancy}")

    keyword = input("Введите ключевое слово для поиска в описании: ")
    keyword_vacancies = [vacancy for vacancy in vacancies if keyword.lower() in vacancy.description.lower()]
    print(f"Вакансии с ключевым словом '{keyword}' в описании:")
    for i, vacancy in enumerate(keyword_vacancies, start=1):
        print(f"{i}. {vacancy}")


if __name__ == "__main__":
    interact_with_user()
