from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, is_admin={self.is_admin})"

    @staticmethod
    def get_user(user_email: str):
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
    def get_cv_by_user_id(user_id: int):
        for cv in cvs_list:
            if cv.user_id == user_id:
                return cv
        return None

    @staticmethod
    def get_cv_by_id(cv_id: int):
        for cv in cvs_list:
            if cv.id == cv_id:
                return cv
        return None


cvs_list = [
    Cv(
        id=1,
        user_id=1,
        full_name="John Doe",
        title="Software Engineer",
        about_me="Experienced developer",
        experience=[
            {
                "company": "Tech Corp",
                "position": "Backend Developer",
                "start_date": "2020-01-01",
                "end_date": "2022-06-30",
                "description": "Developed REST APIs with Flask and FastAPI",
            },
            {
                "company": "Web Solutions",
                "position": "Junior Developer",
                "start_date": "2018-05-01",
                "end_date": "2019-12-31",
                "description": "Maintained front-end apps using React",
            },
        ],
        education=[
            {
                "institution": "University of Technology",
                "degree": "BSc Computer Science",
                "start_date": "2014-08-01",
                "end_date": "2018-05-30",
                "description": "Focused on software development and algorithms",
            }
        ],
        skills=[
            {"name": "Python", "level": 5},
            {"name": "JavaScript", "level": 4},
            {"name": "Flask", "level": 5},
        ],
    )
]

users_list = []
