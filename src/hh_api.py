import requests

from src.api_abstarct import AbstractAPI
from src.vacancy import Vacancy


class HeadHunterAPI(AbstractAPI):
    def __init__(self, api_url: str):
        """
        Конструктор для подключения к hh.ru
        :param api_url: api ссылка для подключения
        """
        self.api_url = api_url

    def connect(self):
        """
        Метод вывода подключения
        :return: нет
        """
        print('Подключение к HH.ru API...')

    def get_vacancies(self, keyword: str, per_page=99):
        """
        Метод для получения вакансий с ссылки api
        :param keyword: ключевое слово для поиска
        :param per_page: количество выводимых вакансий
        :return: список вакансий - vacancies
        """
        params = {
            'per_page': per_page,
            'text': keyword,
            'search_field': ('name', 'description')
        }
        response = requests.get(self.api_url, params).json()
        vacancies = []
        for item in response.get('items', []):
            if keyword.lower() in item.get('name', '').lower():
                salary_data = item.get('salary')
                if salary_data:
                    if salary_data.get('from') is not None and salary_data.get('to') is not None:
                        salary = (salary_data.get('from') + salary_data.get('to')) / 2
                    elif salary_data.get('from') is not None:
                        salary = salary_data.get('from')
                    elif salary_data.get('to') is not None:
                        salary = salary_data.get('to')
                    else:
                        salary = None
                else:
                    salary = None

                vacancy_data = {
                    'name': item.get('name'),
                    'url': item.get('url'),
                    'salary': salary,
                    'description': item.get('description'),
                    'requirement': item.get('snippet', {}).get('requirement', '')
                }
                vacancies.append(Vacancy(**vacancy_data))
        return vacancies

# a = HeadHunterAPI('https://api.hh.ru/vacancies')
# b = [i for i in a.get_vacancies('Python')]
# for i, vacancy in enumerate(b, start=1):
#     print(f'{i}. {vacancy}')