import json
import pyrebase

from chalice import Blueprint
from chalicelib.utils.ssm import get_credential

extra_routes_signup = Blueprint(__name__)
creds = get_credential(parameter="firebase-client")
firebase = pyrebase.initialize_app(json.loads(creds)).auth()

@extra_routes_signup.route("/signup", methods=["POST"])
def signup():
    try:
        body = extra_routes_signup.current_request.json_body
        user = firebase.create_user_with_email_and_password(
            email=body.get('email'),
            password=body.get('password')
        )
        return user
    except Exception as e:
        return {"error": str(e)}