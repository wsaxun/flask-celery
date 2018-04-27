from flask import Blueprint

api_0_2_bp = Blueprint('api_v_0_2',__name__)

VERSION = '0.2'

from . import nbu_api
