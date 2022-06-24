from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

API_CATEGORY = "Auth"

authorization_header = {
    "Authorization": {
        "description":
        "Autorization HTTP header with JWT access token,\
        like: Autorization: Bearer header.payload.signature",
        "in":
        "header",
        "type":
        "string",
        "required":
        True
    }
}

from dorflutter.controllers.auth.signin import *
from dorflutter.controllers.auth.signup import *
from dorflutter.controllers.auth.user import *

