import requests
import yaml

with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

S = requests.Session()


def token_auth(token):
    res = S.get(url=my_dict["url1"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var


def test_step1(login):
    assert 'TestContent' in token_auth(login)


def test_step2(post_new):
    assert 'Anything' in post_new


print(token_auth(my_dict['token']))