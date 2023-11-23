"""Задание 1.
Написать тест с использованием pytest и requests, в котором:
● Адрес сайта, имя пользователя и пароль хранятся в config.yaml;
● conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login
с передачей параметров "username" и "password" и возвращающей токен авторизации;
● Тест с использованием DDT проверяет наличие поста с определенным заголовком
в списке постов другого пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts с хедером, содержащим токен авторизации в
параметре "X-Auth-Token". Для отображения постов другого пользователя передается
"owner": "notMe".
● Добавить тест, в котором создается новый пост, а потом проверяется его наличие
на сервере по полю “описание”."""

import requests


def get_list_descriptions_my_posts(user_url, user_token):
    res_get = requests.get(url=user_url,
                           headers={'X-Auth-Token': user_token},
                           params={'owner': 'Me'}).json()['data']
    return [item['description'] for item in res_get]


def get_list_titles_not_my_posts(user_url, user_token):
    res_get = requests.get(url=user_url,
                           headers={'X-Auth-Token': user_token},
                           params={'owner': 'notMe', 'order': 'ASC'}).json()['data']
    return [item['title'] for item in res_get]
