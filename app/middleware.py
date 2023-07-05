from flask_httpauth import HTTPBasicAuth
from app.service import get_user_by_email,check_password
auth = HTTPBasicAuth()

@auth.verify_password
def protected(username, password):
    user = get_user_by_email(username)

    if not user:    
        return False
    
    if not check_password(password,user.password):
        return False
    
    return True

# Usage example
# @app.route("/admin")
# @auth.login_required
# def admin_home():
    # return "Admin loggedin"