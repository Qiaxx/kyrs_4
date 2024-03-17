from src.hh_api import HeadHunterAPI
from src.json_storage import JSONStorage


def interact_with_user():
    """
    Главный функционал программы
    :return: нет
    """
    # подключение к api
    api = HeadHunterAPI('https://api.hh.ru/vacancies')
    storage = JSONStorage("vacancies.json")

    # запрос слова для поиска вакансий
    query = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")
    api.connect()
    vacancies = api.get_vacancies(query)

    # запрос количества отображаемых вакансий/топ вакансий
    count = int(input("Введите количество вакансий для отображения: "))
    top_n_vacancies = sorted(vacancies, reverse=True)[:count]
    print(f"Топ {count} вакансий по зарплате: ")
    for i, vacancy in enumerate(top_n_vacancies, start=1):
        print(f"{i}. {vacancy}")

    # поиск вакансий по ключевому слову в описании
    keyword = input("Введите ключевое слово для поиска в описании: ")
    keyword_vacancies = [vacancy for vacancy in vacancies if keyword.lower() in vacancy.description.lower()]
    print(f"Вакансии с ключевым словом '{keyword}' в описании: ")
    for i, vacancy in enumerate(keyword_vacancies, start=1):
        print(f"{i}. {vacancy}")

    # сохранение в файл в формате json
    user_questions = input('Желаете сохранить найденные вакансии? (y|n): ')
    if user_questions.lower() == 'y':
        for vacancy in top_n_vacancies:
            storage.add_vacancy(vacancy)
        for vacancy in keyword_vacancies:
            storage.add_vacancy(vacancy)
    else:
        print('Поиск завершен')


if __name__ == "__main__":
    interact_with_user()
