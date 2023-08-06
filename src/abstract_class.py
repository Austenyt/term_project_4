from abc import ABC, abstractmethod


class JobApi(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_vacancies_api(self):
        """Подключение к API и получение вакансий"""
        pass


class JobFile(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy_data):
        """Добавляет информацию о вакансии в JSON-файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Возвращает данные о вакансиях, соответствующие указанным критериям"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        """Удаляет информацию о вакансии из файла по её идентификатору"""
        pass
