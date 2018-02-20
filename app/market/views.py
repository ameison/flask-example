from flask import render_template

from . import market
from ..models import User

@market.route('/market')
def market_page():
    freelancers_list = User.query.all()
    return render_template('market/index.html', freelancers=freelancers_list, title="Marketplace")
