from flask import Blueprint, render_template, request, url_for
from database.database import USERS

user_route = Blueprint('user', __name__)

@user_route.route('/')
def list_users():
    return render_template('users.html', users=USERS)

@user_route.route('/create-user', methods=['POST'])
def new_user():
    name = request.form['name']
    email = request.form['email']
    id = len(USERS) + 1
    USERS.append({'id':id, 'name':name, 'email':email})
    return render_template('form_new_user.html')

@user_route.route('/create-user')
def insert_user():
    return render_template('form_new_user.html')

@user_route.route('/<int:id>/delete', methods=['POST'])
def delete_user(id):
    global USERS
    USERS = [u for u in USERS if u['id'] != id]
    return render_template('users.html', users=USERS)