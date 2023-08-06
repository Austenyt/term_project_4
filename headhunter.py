from src.abstract_class import JobApi

from requests import *


class HeadHunter(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой HeadHunter,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    _api_link = "https://api.hh.ru/vacancies"

    def __str__(self):
        return "headhunter.ru"

    def get_vacancies_api(self, keyword):
        response = get(f'https://api.hh.ru/vacancies?text={keyword}')
        return response.json()['items']
