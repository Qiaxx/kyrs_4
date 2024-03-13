import requests

from src.api_abstarct import AbstractAPI
from src.vacancy import Vacancy


class HeadHunterAPI(AbstractAPI):
    def __init__(self, api_key):
        self.api_key = api_key

    def connect(self):
        print('Подключение к HH.ru API...')

    def get_vacancies(self, keyword, per_page=99):
        params = {
            'per_page': per_page,
            'text': keyword,
            'search_field': ('name', 'description')
        }
        response = requests.get(self.api_key, params=params).json()
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
