from src.abstract_class import JobApi
import os
from requests import *


class SuperJob(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии superjob.ru"""

    __API_KEY = os.getenv('SJ_API_KEY')
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __str__(self):
        return "superjob.ru"

    def get_vacancies_api(self, keyword):

        params = {
            "keyword": keyword,
            "page": "1"
        }
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }

        response = get(self._api_link, headers=headers, params=params)
        return response.json()['objects']

    def get_region_vacancies(self, keyword):
        response = get(f'https://api.hh.ru/vacancies?text={keyword}')
        return response.json()['items']