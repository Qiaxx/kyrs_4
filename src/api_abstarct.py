from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def get_vacancies(self, keyword):
        pass
