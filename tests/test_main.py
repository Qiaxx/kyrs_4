import pytest
from src.vacancy import Vacancy
from src.hh_api import HeadHunterAPI
from src.json_storage import JSONStorage
from main import interact_with_user


@pytest.fixture
def api_mock():
    return HeadHunterAPI


@pytest.fixture
def storage_mock():
    return JSONStorage


def test_interact_with_user(monkeypatch, capsys, api_mock, storage_mock):
    monkeypatch.setattr('builtins.input', lambda _: 'python developer')

    # Моки возвращают предопределенные значения
    api_mock.get_vacancies.return_value = [
        Vacancy("Python Developer", "https://example.com", 100000, "Python developer job description",
                "Django experience required"),
        Vacancy("Senior Python Developer", "https://example.com", 150000, "Senior Python developer job description",
                "Flask experience required"),
        Vacancy("Django Developer", "https://example.com", 120000, "Django developer job description",
                "Python experience required")
    ]
    storage_mock.get_vacancies = []

    # Подменяем создание объектов на наши моки
    monkeypatch.setattr('src.hh_api.HeadHunterAPI', api_mock)
    monkeypatch.setattr('src.json_storage.JSONStorage', storage_mock)

    # Подменяем стандартный ввод пользовательских данных
    monkeypatch.setattr('builtins.input', lambda _: '3')

    interact_with_user()

    out, _ = capsys.readouterr()
    assert "Топ 3 вакансий по зарплате:" in out
    assert "1. Senior Python Developer" in out
    assert "2. Django Developer" in out
    assert "3. Python Developer" in out
    assert "Вакансии с ключевым словом 'django' в описании:" in out
    assert "1. Django Developer" in out
