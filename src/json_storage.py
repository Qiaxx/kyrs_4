from src.abstarct_vanacy import VacancyAbstarct
import json


class JSONStorage(VacancyAbstarct):
    def __init__(self, file_path):
        """
        Конструктор для создания json файла с вакансиями
        :param file_path: файл с вакансиями или название для создания нового файла с вакансиями
        """
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        """
        Метод добавления в файл вакансию
        :param vacancy: вакансия (экземпляр)
        :return: нет
        """
        with open(self.file_path, 'a') as file:
            json.dump(vars(vacancy), file)
            file.write('\n')

    def get_vacancies(self, **criteria):
        """
        Метод получения/вывода вакансии
        :param criteria: параметр получения всех ключей
        :return: список вакансий
        """
        vacancies = []
        with open(self.file_path, 'r') as file:
            for line in file:
                data = json.loads(line)
                if all(data.get(key) == value for key, value in criteria.items()):
                    vacancies.append(data)
        return vacancies

    def remove_vacancy(self, vacancy_id):
        """
        Метод удаления вакансии
        :param vacancy_id: идентификатор вакансии
        :return: нет
        """
        vacancies = []
        with open(self.file_path, 'r') as file:
            for line in file:
                data = json.loads(line)
                if data.get('id') != vacancy_id:
                    vacancies.append(data)
        with open(self.file_path, 'w') as file:
            for vacancy in vacancies:
                json.dump(vacancy, file)
                file.write('\n')
