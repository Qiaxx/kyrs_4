from abc import ABC, abstractmethod


class VacancyAbstarct(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **criteria):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        pass
