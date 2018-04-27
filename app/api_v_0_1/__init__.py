from flask import Blueprint

api_bp = Blueprint('api_v_0_1',__name__)

VERSION = '0.1'

from . import nbu_api,other_api
