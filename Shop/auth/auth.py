from flask import Blueprint, render_template, flash
from auth.forms import RegisterForm
from sql.db import DB

from auth.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

auth = Blueprint('auth', __name__, url_prefix='/',template_folder='templates')

def check_duplicate(e):

    import re
    r = re.match(".*IS601_Users.(\w+)", e.args[0].args[1])
    if r:
        flash(f"The chosen {r.group(1   )} is not available", "warning")
    else:
        flash("Unknown error occurred, please try again", "danger")
        print(e)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    # wtform validators are both client-side and server-side
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        try:
            hash = bcrypt.generate_password_hash(password)
            # save the hash, not the plaintext password
            result = DB.insertOne("INSERT INTO IS601_Users (email, username, password) VALUES (%s, %s, %s)", email, username, hash)
            if result.status:
                flash("Successfully registered","success")
        except Exception as e:
            check_duplicate(e)
    return render_template("register.html", form=form)
