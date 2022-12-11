# from https://towardsdatascience.com/deploy-to-google-cloud-run-using-github-actions-590ecf957af0
import os
import sys
from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()
import flask_login
from flask_login import current_user
from flask_caching import Cache
# added so modules can be found between the two different lookup states:
# from tests and from regular running of the app
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
print(CURR_DIR)
sys.path.append(CURR_DIR)

# custom error pages
def page_not_found(e):
    return render_template('404.html'), 404

def permission_denied(e):
    return render_template("403.html"), 403

def unauthorized(e):
    return render_template("401.html"), 401


login_manager = flask_login.LoginManager()
# app = Flask(__name__)
def create_app(config_filename=''):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, permission_denied)
    app.register_error_handler(401, unauthorized)
    app.secret_key = os.environ.get("SECRET_KEY", "missing_secret")
    app.cache = Cache(app,config={'CACHE_TYPE': 'SimpleCache'})
    login_manager.init_app(app)
    # app.config.from_pyfile(config_filename)
    with app.app_context():
        from auth.auth import auth
        app.register_blueprint(auth)

        @login_manager.user_loader
        def load_user(user_id):
            if user_id is None:
                return None
            print("login_manager loading user") # happens each request
            from auth.models import User
            from sql.db import DB
            try:
                result = DB.selectOne("SELECT id, email, username FROM IS601_Users WHERE id = %s", user_id)
                if result.status:
                    return User(**result.row)
            except Exception as e:
                print(e)
            return None

        # DON'T DELETE, this cleans up the DB connection after each request
        # this avoids sleeping queries
        @app.teardown_request 
        def after_request_cleanup(ctx):
            from sql.db import DB
            DB.close()
        return app




app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
