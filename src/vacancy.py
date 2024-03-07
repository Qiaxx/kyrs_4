class Vacancy:

    def __init__(self, name, url, salary: int, description, requirement):
        self.name = name
        self.url = url
        if salary is not None:
            self.salary = salary
        else:
            self.salary = 0
        self.description = description
        self.requirement = requirement

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __repr__(self):
        return f"Vacancy(name='{self.name}', url='{self.url}', salary={self.salary}, description='{self.description}', requirement='{self.requirement}')"

    def __str__(self):
        return f"Название: {self.name}\nURL: {self.url}\nЗарплата: {self.salary}\nОписание: {self.description}\nТребования: {self.requirement}"
