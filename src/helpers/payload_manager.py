# payloads for all different types of requests

def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_put_booking():
    payload = {
        "firstname": "Sumanth",
        "lastname": "Sure",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_mild_booking():
    payload = {
        "firstname": "Sssss",
        "lastname": "Broooooo",
        "totalprice": 145
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
