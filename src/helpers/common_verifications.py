# status code

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected https Status code" + expect_data


# body verification
def verify_json_key_not_null(key):
    assert key != '0', "Key is not zero" + key
    assert key > 0, "Key is greater than zero" + key


# response verification

def verify_response_key_should_not_be_none(key):
    assert key is not None



