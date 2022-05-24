import uuid

import requests


def post_event(data: dict):
    return requests.post('http://127.0.0.1:8002/event/tt', json=data)


if __name__ == '__main__':
    test_obj = {
        'id': str(uuid.uuid4()),
        'type': 1
    }
    resp = post_event(test_obj)
    print(resp.status_code)
    print(resp.json())

