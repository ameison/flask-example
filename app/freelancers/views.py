__author__ = 'poseidon'
from flask import render_template

from . import freelancers
from ..models import User


@freelancers.route('/freelancers')
def freelancers_page():
    freelancers_list = User.query.filter(User.tipo_usuario == User.FREELANCE).all()
    return render_template('freelancers/index.html', freelancers=freelancers_list, title="Freelancers")