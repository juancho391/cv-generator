from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from .forms import SigNupForm, LoginForm, CVForm
from .models import User, Cv, users_list, cvs_list
import os

template_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates"
)
app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "mysecretkeyultrasecure"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users_list if int(user.id) == int(user_id)), None)


@app.route("/")
@login_required
def index():
    return render_template("index.html", cvs=cvs_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = SigNupForm()
    if form.validate_on_submit():
        new_user = User(
            id=len(users_list) + 1,
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )

        if User.get_user(new_user.email):
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for("login"))
        new_user.set_password(form.password.data)
        users_list.append(new_user)
        flash(f"User {new_user.name} registered successfully!", "success")
        return redirect(url_for("login"))
    print("register form errors:", form.errors)
    return render_template("/admin/signup_form.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Logged in successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid email or password", "danger")
    return render_template("login_form.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "info")
    return redirect(url_for("index"))


@app.route("/cv/<int:cv_id>", methods=["GET"])
@login_required
def view_cv(cv_id):
    cv = Cv.get_cv_by_id(cv_id)
    if not cv:
        flash("CV not found", "danger")
        return redirect(url_for("index"))
    return render_template("cv_view.html", cv=cv)


@app.route("/cv/create", methods=["GET", "POST"])
@login_required
def create_cv():
    form = CVForm()
    if form.validate_on_submit():
        new_cv = Cv(
            id=len(cvs_list) + 1,
            user_id=current_user.id,
            full_name=form.full_name.data,
            title=form.title.data,
            about_me=form.about_me.data,
            experience=[exp.data for exp in form.experience],
            education=[edu.data for edu in form.education],
            skills=[skill.data for skill in form.skills],
        )
        print(new_cv.to_dict)
        cvs_list.append(new_cv)
        flash("CV created successfully!", "success")
        return redirect(url_for("index"))
    print("CV form errors:", form.errors)
    return render_template("/admin/cv_form.html", form=form)
