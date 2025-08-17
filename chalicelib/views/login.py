import json
import pyrebase

from chalice import Blueprint
from chalicelib.utils.ssm import get_credential

extra_routes_login = Blueprint(__name__)
creds = get_credential(parameter="firebase-client")
firebase = pyrebase.initialize_app(json.loads(creds)).auth()

@extra_routes_login.route("/login", methods=["POST"])
def login():
        try:
            body = extra_routes_login.current_request.json_body
            user = firebase.sign_in_with_email_and_password(
                email=body.get('email'),
                password=body.get('password')
            )
            return user
        except Exception as e:
            return {"error": str(e)}                                                    