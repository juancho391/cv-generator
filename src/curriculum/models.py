from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

cvs_list = []
users_list = []


class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def set_password(self, new_password) -> None:
        self.password = generate_password_hash(new_password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, is_admin={self.is_admin})"

    @staticmethod
    def get_user(user_email: str) -> "User" | None:
        for user in users_list:
            if user.email == user_email:
                return user
        return None


class Cv:
    def __init__(
        self, id, user_id, full_name, title, about_me, experience, education, skills
    ):
        self.id = id
        self.user_id = user_id
        self.full_name = full_name
        self.title = title
        self.about_me = about_me
        self.experience = experience
        self.education = education
        self.skills = skills

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "title": self.title,
            "about_me": self.about_me,
            "experience": self.experience,
            "education": self.education,
            "skills": self.skills,
        }

    @staticmethod
    def get_cv_by_user_id(user_id: int) -> "Cv" | None:
        for cv in cvs_list:
            if cv.user_id == user_id:
                return cv
        return None

    @staticmethod
    def get_cv_by_id(cv_id: int) -> "Cv" | None:
        for cv in cvs_list:
            if cv.id == cv_id:
                return cv
        return None
