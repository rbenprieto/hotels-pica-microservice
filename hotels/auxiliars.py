from requests import request


def validate_token(token: str) -> bool:
    if token:
        response = request(
            method="POST",
            url="http://authorization/api/auth/validate",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={"token": token},
        )
        if response.status_code == 200 and response.json():
            return True
    return False
