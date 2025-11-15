import requests


Base_url = 'https://ru.yougile.com/api-v2'
Token = 'EAyNKuFGBHt4gycCGTsxkI0TNZgRt5-50nQLpjEg8Dc3M24-xn6bCMHaMmiQqs5P'
Headers = {'Authorization': f'Bearer {Token}'}


# создание проекта, позитивный тест
def test_create_project_positive():
    body = {
        'title': 'new project'
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    assert resp.status_code == 201
    assert result['id'] is not None


# создание проекта, негативный тест, отсутствует обязательное поле "title", тест падает
def test_create_project_negative():
    body = {
        
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    assert resp.status_code == 400 


# изменение проекта, позитивный тест
def test_change_project_positive():
    # cоздаём проект
    body = {
        'title': 'new project'
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    id = result['id']
    # изменяем название проекта
    new_body = {
        'title': 'change project'
    }
    resp = requests.put(f'{Base_url}/projects/{id}', json=new_body, headers=Headers)
    new_result = resp.json()
    assert resp.status_code == 200
    assert new_result['id'] is not None


# изменение проекта, негативный тест, запрос с неверным ID, тест падает
def test_change_project_negative():
    # cоздаём проект
    body = {
        'title': 'new project'
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    id = result['id']
    # изменяем название проекта
    new_body = {
        'title': 'change project'
    }
    resp = requests.put(f'{Base_url}/projects/{id + 'abc'}', json=new_body, headers=Headers)
    resp.json()
    assert resp.status_code == 404


# получение проекта по id, позитивный тест
def test_get_project_id_positive():
    # создаём проект
    body = {
        'title': 'new project 2'
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    id = result['id']
    
    # получаем проект по id
    resp = requests.get(f'{Base_url}/projects/{id}', headers=Headers)
    new_result = resp.json()
    assert resp.status_code == 200
    assert new_result['id'] is not None
    assert new_result['title'] == 'new project 2'
    assert new_result['timestamp'] is not None


# получение проекта по ID, негативный тест, неверный ID в запросе, тест падает
def test_get_project_id_negative():
    # создаём проект
    body = {
        'title': 'new project 2'
    }
    resp = requests.post(f'{Base_url}/projects', json=body, headers=Headers)
    result = resp.json()
    id = result['id']
    
    # получаем проект по id
    resp = requests.get(f'{Base_url}/projects/{id + 'cde'}', headers=Headers)
    resp.json()
    assert resp.status_code == 404

