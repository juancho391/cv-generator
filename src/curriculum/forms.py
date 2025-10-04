from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField,
    IntegerField,
    DateField,
    FieldList,
    FormField,
)
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional


class SigNupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class ExperienceForm(FlaskForm):
    company = StringField("Company", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()], format="%Y-%m-%d")
    end_date = DateField("End Date", validators=[Optional()], format="%Y-%m-%d")
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])


class EducationForm(FlaskForm):
    institution = StringField("Institution", validators=[DataRequired()])
    degree = StringField("Degree", validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()], format="%Y-%m-%d")
    end_date = DateField("End Date", validators=[Optional()], format="%Y-%m-%d")
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])


class SkillForm(FlaskForm):
    name = StringField("Skill", validators=[DataRequired()])
    level = IntegerField(
        "Level", validators=[DataRequired(), NumberRange(min=1, max=5)]
    )


class CVForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    about_me = TextAreaField("About Me", validators=[Optional(), Length(max=1000)])

    experience = FieldList(FormField(ExperienceForm), min_entries=1, max_entries=10)
    education = FieldList(FormField(EducationForm), min_entries=1, max_entries=10)
    skills = FieldList(FormField(SkillForm), min_entries=1, max_entries=20)

    submit = SubmitField("Save CV")
