from . import db
from .models import User
from .models import Userd
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/new')
@login_required
def new_user_profile():
    return render_template('user.html')


@main.route('/new', methods=['POST'])
@login_required
def new_user_post():
    name = request.form.get('name')
    age = request.form.get('age')
    bg = request.form.get('bg')
    gender = request.form.get('gender')
    height = request.form.get('height')
    weight = request.form.get('weight')
    phone = request.form.get('phone')
    address = request.form.get('address')
    availablity = request.form.get('availablity')
    lastdonation = request.form.get('lastdonation')
    degree = request.form.get('degree')
    
    userd = Userd(name=name,age=age,bg=bg,gender=gender,height=height,weight=weight,
    phone=phone,address=address,availablity=availablity,
    lastdonation=datetime.strptime(lastdonation, "%Y-%m-%d").date(),
    degree=degree ,author=current_user)
    db.session.add(userd)
    db.session.commit()
    #teacher.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()


    flash('Your details has been added!')

    return redirect(url_for('main.user_workouts'))

@main.route('/donating')
@login_required
def donating():
    return render_template('userdetails.html')



@main.route('/all')
@login_required
def user_workouts():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    usersd = user.usersd
    return render_template('userdetails.html', usersd=usersd, user=user)