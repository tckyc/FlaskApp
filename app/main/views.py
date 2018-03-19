from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from app.models import User
from app.email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            users_role = User.query.filter_by(username='susan').first().role
            user_db = User(username=form.name.data, role=users_role)
            db.session.add(user_db)
            db.session.commit()
            session['known'] = False
            if current_app.config['BLOG_MAIL_USERER']:
                send_email(current_app.config['BLOG_MAIL_USERER'], form.name.data, 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow(),
                           known=session.get('known', False))
