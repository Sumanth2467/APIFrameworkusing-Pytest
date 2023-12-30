from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests, patch_requests, delete_requests
from src.helpers.common_verifications import verify_http_status_code
from src.helpers.common_verifications import verify_response_key_should_not_be_none
from src.helpers.payload_manager import payload_create_booking
from src.helpers.payload_manager import payload_create_token
from src.helpers.utils_headers import common_headers_json
from src.helpers.api_request_wrapper import put_requests
from src.helpers.utils_headers import common_headers_for_put
from src.helpers.payload_manager import payload_put_booking
from src.helpers.payload_manager import payload_mild_booking

import pytest

class TestCrudBooking:

    @pytest.fixture()
    def test_create_token(self):
        response = post_requests(url=APIConstants.url_create_token(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_token(), in_json=False)
        print(response)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        print(token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def test_create_booking(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid


    def test_update_booking(self,test_create_token,test_create_booking):
        bookingId = test_create_booking
        put_url = APIConstants.url_create_booking() +"/"+ str(bookingId)
        response = put_requests(url=put_url, auth=None, headers=common_headers_for_put(), payload=payload_put_booking(),in_json=False)
        print(response.json())

    def test_mild_update_booking(self,test_create_token,test_create_booking):
        bookingId = test_create_booking
        put_url = APIConstants.url_create_booking() + "/" + str(bookingId)
        response = patch_requests(url=put_url, auth=None, headers=common_headers_for_put(), payload=payload_mild_booking(),
                                in_json=False)
        print(response.json())

    def test_delete_booking(self,test_create_token,test_create_booking):
        bookingId = test_create_booking
        delete_url = APIConstants.url_create_booking() + "/" + str(bookingId)
        response = delete_requests(url=delete_url, auth=None, headers=common_headers_for_put(), payload={},
                                in_json=False)
        print(response)
ls
