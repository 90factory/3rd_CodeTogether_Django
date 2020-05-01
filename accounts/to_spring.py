import requests
import json


def to_spring_test(url, data):
    r = requests.post(f'http://127.0.0.1:9000/{url}/', json=data)
    return r.json()


def to_spring(url, data):
    r = requests.post(f'http://192.168.21.129:8080/{url}', json=data)
    return r.json()