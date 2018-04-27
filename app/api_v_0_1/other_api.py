from flask import request,jsonify
from . import api_bp as api
from ..models import User
from ..email import send_email
from app import db


@api.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        request_json = request.json
        email = request_json['email']
        username = request_json['username']
        password = request_json['password']
        confirm_password = request_json['confirm_password']
        token = None
        if password == confirm_password and username is not None and email is not None:
            user = User(name=username,email=email,password=password)
            try:
                db.session.add(user)
                db.session.commit()
                token = user.generate_auth_token()
                # send_email(user.email, '验证你的邮箱', 'auth/email/confirm', user=user, token=token)
            except Exception as ex:
                db.session.rollback()
                return jsonify({
                    'status':'false',
                    'error':str(ex),
                    'params':request_json
                })
        return jsonify({
            'status':'true',
            'msg':'email need to verify.',
            'token':str(token,encoding='utf-8'),
            'params':request_json
        })

# @api.route('/confirm/<token>')
# @login_required
# def confirm(token):
#     if current_user.confirmed:
#         return redirect(url_for('main.home'))
#     if current_user.confirm(token):
#         db.session.commit()
#         flash('You have confirmed your account. Thanks!')
#     else:
#         flash('The confirmation link is invalid or has expired.')
#     return redirect(url_for('main.home'))
