import requests
import json


def user_authentication(func):
    def wrapper():

        member_id = 1
        params = {'member_id': member_id}
        params = json.dumps(params)
        print(type(params))
        r = requests.post(url='http://localhost:9000/create/', data=params)
        print('hi')
        print(r.json())
        print(r.url)
        return func()
    return wrapper()