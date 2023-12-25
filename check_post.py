import requests
import yaml
import logging

with open('testdata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path_login']
    try:
        post = requests.post(url=path, data={'username': data['login'], 'password': data['password']})
        token = post.json()['token']
        logging.info(f"We get {token}")
        return post.json()['token']
    except:
        logging.exception(f"Exception with get login")
        return None


def get_post(token):
    path = data['path_post']
    try:
        get = requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
        logging.info(f"We get post")
        return get.json()
    except:
        logging.exception(f"Exception with get post")
        return None


def create_post(token):
    path = data['path_post']
    try:
        post = requests.post(url=path, params={'title': data['title'], 'description': data['description'],
                                               'content': data['content']}, headers={"X-Auth-Token": token})
        logging.info(f"We create post")
        return post.json()
    except:
        logging.exception(f"Exception with create post")
        return None


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    print(create_post(token))