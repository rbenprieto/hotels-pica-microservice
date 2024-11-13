from requests import request


def validate_token(token: str) -> bool:
    if token:
        response = request(
            method="POST",
            url="http://authorization:8083/api/auth/validate",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={"token": token},
        )
        print(response.__dict__)
        print(response.request)
        if response.status_code == 200 and response.json():
            return True
    return False
