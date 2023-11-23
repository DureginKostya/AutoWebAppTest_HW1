import pytest
import yaml
import requests

with open('config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def create_my_post(get_token):
    return requests.post(url=data['url_post'],
                         headers={'X-Auth-Token': get_token},
                         params={'owner': 'Me',
                                 'title': data['title_my_post'],
                                 'description': data['description_my_post'],
                                 'content': data['content_my_post']})


@pytest.fixture(autouse=True, scope='class')
def get_info_my_post():
    return data['url_post'], data['description_my_post']


@pytest.fixture(autouse=True, scope='class')
def get_info_not_my_post():
    return data['url_post'], data['title_not_my_post']


@pytest.fixture(autouse=True, scope='class')
def get_token():
    return requests.post(url=data['url_login'],
                         data={'username': data['login'], 'password': data['passwd']}).json()['token']
