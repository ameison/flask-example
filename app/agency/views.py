__author__ = 'poseidon'
from flask import render_template

from . import agency


@agency.route('/agency')
def agency_page():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('agency/index.html', title="Agencias")