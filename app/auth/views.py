from flask import flash, redirect, render_template, url_for

from . import auth
from ..util import code_generator
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        my_user = User()
        my_user.categoria_id = '1'
        my_user.codigo = code_generator(6)
        my_user.clave = '123456'
        my_user.correo = form.email.data
        my_user.nombres = form.first_name.data
        my_user.apellidos = form.last_name.data
        my_user.pais_id = form.country.data
        my_user.telefono = '5464654'
        my_user.tipo_usuario = 'FR'
        db.session.add(my_user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('home.home_page'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Registrar')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            # guardar en local storage el token y redirect a admin.

            # redirect to the dashboard page after login
            return redirect(url_for('home.home_page'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

