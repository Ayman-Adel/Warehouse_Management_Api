import time
from decouple import config
import jwt
import os
from dotenv import load_dotenv
load_dotenv()
# config("secret")

jwt  = jwt.api_jwt
jwt_secret = str(os.getenv('secret'))
jwt_algorithm = str(os.getenv('algorithm'))

# returns generated token


def token_response(token: str):
    return {
        "access token": token
    }


def signjwt(useremail: str):
    payload = {
        "user email": useremail,
        "expiry": time.time()+600
    }
    token = jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)
    return token_response(token.decode("utf-8"))


def decodejwt(token: str):
    try:
        decode_token = jwt.decode(token, jwt_secret, algorithm=jwt_algorithm)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
