from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png'], 'Upload a .png or .jpg file')])
