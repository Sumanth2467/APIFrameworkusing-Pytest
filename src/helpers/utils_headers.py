# Common headers

# for jason format
def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def common_headers_for_put():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers



# for XML format
def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers
