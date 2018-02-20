from flask import render_template

from . import home


@home.route('/')
def home_page():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/index.html', title="Inicio")