from chalice import Chalice
from chalicelib.views.signup import extra_routes_signup
from chalicelib.views.login import extra_routes_login

app = Chalice(app_name='auth-microsservice')
app.register_blueprint(extra_routes_signup)
app.register_blueprint(extra_routes_login)