from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.utils_headers import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verifications import verify_response_key_should_not_be_none
from src.helpers.common_verifications import verify_http_status_code
import requests
import pytest


class TestCreateBooking:
    def test_create_booking1(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(), payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid=response.json()["bookingid"]
        print(bookingid)

    def test_create_booking2(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(), payload=None, in_json=False)

        verify_http_status_code(response, 400)
        print(response.status_code)

    def test_create_booking3(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(), payload={}, in_json=False)

        verify_http_status_code(response, 500)
        print(response.status_code)


 