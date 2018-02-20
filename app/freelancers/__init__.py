__author__ = 'poseidon'

from flask import Blueprint

freelancers = Blueprint('freelancers', __name__)

from . import views