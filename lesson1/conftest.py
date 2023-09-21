import pytest
import yaml
import requests


with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

S = requests.Session()

@pytest.fixture()
def login():
    obj_data = S.post(url=my_dict['url'], data={'username': 'IvanP', 'password': 'e794244c93'})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post_new():
    obj_data = S.post(url=my_dict['url1'], headers={"X-Auth-Token": my_dict['token']}, data={
        'username': 'IvanP',
        'password': 'e794244c93',
        'title': 'newPost',
        'description': 'Anything',
        'content': 'we will see'})
    return obj_data.json()['description']