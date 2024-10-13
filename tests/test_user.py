

from utils import requestmethods
from utils.requestmethods import APIRequestMethods
import pytest
import requests
from utils.file_loader import load_json_file

@pytest.mark.smoke
@pytest.mark.regression
def test_list_all_users(base_url):
    expected_response = load_json_file('/Users/vikashmishra/Desktop/ReqResAutomation/test_data/list_all_users.json')
    response = requests.get(base_url + '/users?page=2' )
    data = response.json()
    print(data)
    assert data == expected_response
    assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.sanity
def test_single_user(base_url):
    expected_response = load_json_file('/Users/vikashmishra/Desktop/ReqResAutomation/test_data/single_user.json')
    response = requests.get(base_url + '/users/2')
    data = response.json()
    print(data)
    assert data == expected_response
    assert response.status_code == 200

@pytest.mark.sanity
@pytest.mark.smoke
def test_single_user_not_found(base_url):
    response = requests.get(base_url + '/users/23')
    data = response.json()
    print(data)
    assert response.status_code == 404
    assert data == {}


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_create_user(base_url):
    user_data = load_json_file('/Users/vikashmishra/Desktop/ReqResAutomation/test_data/create_data.json')
    response = requests.post(base_url + '/users',json=user_data)
    data=response.json()
    print('response_data :', data)
    assert response.status_code == 201

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_update_user(base_url):
    user_data = load_json_file('/Users/vikashmishra/Desktop/ReqResAutomation/test_data/user_data.json')['update_user']
    response = requests.put(base_url + '/users/2', json=user_data)
    data = response.json()
    print('response_data :', data)
    assert response.status_code == 200
    assert data ['job'] == 'QA Engineer'

@pytest.mark.regression
def test_partial_update(base_url):
    user_data = load_json_file('/Users/vikashmishra/Desktop/ReqResAutomation/test_data/user_data.json')['patch_data']
    response = requests.patch(base_url + '/users/2', json=user_data)
    data = response.json()
    print('response_data :', data)
    assert response.status_code == 200
    assert data ['name'] == 'morpheus'
    assert data['job'] == 'zion resident'

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_delete_user(base_url):
    response = requests.delete(base_url + '/users/2')
    assert response.status_code == 204
    if response.status_code == 204:
        print ('user deleted successfully')







