import requests


def test_post():
    response = requests.post(
        url="https://petstore.swagger.io/v2/pet",
        json={
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "EkaterinaSerggeevna345",
            "photoUrls": ["string"],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        },
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    print(response.status_code)
    print(response.json())


def test_get():
    response = requests.get(
        url="https://petstore.swagger.io/v2/pet/9223372036854776000",
        headers={
            "Accept": "application/json"
        }
    )

    print(response.status_code)
    print(response.json())


def test_put():
    response = requests.put(
        url='https://petstore.swagger.io/v2/pet',
        json={
            "id": 9223372036854776000,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie123",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        },
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    print(response.status_code)
    print(response.json())


def test_delete():
    response = requests.delete(
        url='https://petstore.swagger.io/v2/pet/9223372036854776000',
        headers={
            "Accept": "application/json"
        }
    )
    print(response.status_code)
    print(response.json())


test_post()
test_get()
test_put()
test_delete()
