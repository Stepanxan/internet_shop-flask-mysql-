from flask import request, flash, url_for, redirect, render_template
from werkzeug.security import generate_password_hash

from libs.db import *
from libs.conf import app


tbl_users_schema = TblUsersSchema()
tbl_users_schemas = TblUsersSchema(many=True)

@app.route('/registration', methods=['POST'])
def registration():
        id = request.form.get('id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        password2 = request.form.get('password2')


        if request.method == 'POST':
            if password != password2:
                flash("Паролі не співпадають", category='error')
                return redirect(url_for('registration'))
            else:
                has_password = generate_password_hash(password)
                tbl_users_schema = TblUsersSchema(
                    id=id,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    password=has_password
                )

                try:
                    db.session.add(tbl_users_schema)
                    db.session.commit()
                    flash("Реєстрація пройшла успішно", category='success')
                    return redirect(url_for('login'))
                except:
                    flash("Користувач з таким email вже існує", category='error')
                    return redirect(url_for('registration'))

        else:
            return render_template('registration.html')