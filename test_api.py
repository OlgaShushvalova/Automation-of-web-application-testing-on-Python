import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

S = requests.Session()


def test_post_create(login):
    res = S.post(url= testdata['post_address'], headers={'X-Auth-Token': login},
           data={'title':  testdata['title'], 'description':  testdata['description'], 'content':  testdata['content']})
    logging.debug(f"Response is {str(res)}")
    assert str(res) == '<Response [200]>', 'post_create FAIL'


def test_check_post(login):
    result = S.get(url=testdata['api_address'], headers={'X-Auth-Token': login}).json()['data']
    logging.debug(f"get request return: {result}")
    list_description = [i['description'] for i in result]
    assert  testdata['description'] in list_description, 'check_post_create FAIL'


def test_check_post_notmy(login):
    result = S.get(url=testdata['api_address'], headers={'X-Auth-Token': login}, params={'owner': 'notMe'}).json()['data']
    logging.debug(f"get request return: {result}")
    result_title = [i['title'] for i in result]
    assert testdata['not_my_post'] in result_title, 'check not my post FAIL'