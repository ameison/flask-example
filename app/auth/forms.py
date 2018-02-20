from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    primary_use = RadioField(None, choices=[('CL', 'Contratar un servicio'), ('FR', 'Trabajar como freelance')],
                             default='CL')

    first_name = StringField(None, validators=[DataRequired("Debe ingresar su nombre")],
                             render_kw={"placeholder": "Nombres"})
    last_name = StringField(None, validators=[DataRequired("Debe ingresar sus apellidos")],
                            render_kw={"placeholder": "Apellidos"})
    country = SelectField(None, choices=[('1', 'Perú'), ('2', 'México')])
    email = StringField(None, validators=[Email("Debe ingresar un correo válido")],
                        render_kw={"placeholder": "Correo"})
    password = PasswordField(None, validators=[DataRequired("Debe ingresar una contraseña"),
                                               EqualTo('confirm_password', message='Las contraseñas no coincidem')],
                             render_kw={"placeholder": "Ingrese su contraseña"})
    confirm_password = PasswordField(None, render_kw={"placeholder": "Repita su contraseña"})
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if User.query.filter_by(correo=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')