from flask import Blueprint, render_template, request, url_for
from database.database import USERS

user_route = Blueprint('user', __name__)

@user_route.route('/')
def list_users():
    return render_template('users.html', users=USERS)

@user_route.route('/create-user', methods=['POST'])
def form_insert_user():
    name = request.form['name']
    email = request.form['email']
    id = len(USERS) + 1
    USERS.append({'id':id, 'name':name, 'email':email})
    return render_template('form_insert_user.html')

@user_route.route('/create-user')
def insert_user():
    return render_template('form_insert_user.html')

@user_route.route('/<int:id>/delete', methods=['POST'])
def delete_user(id):
    global USERS
    USERS = [u for u in USERS if u['id'] != id]
    return list_users()

@user_route.route('/<int:id>/update')
def form_update_user(id):
    global USERS
    old_name = USERS[id]['name']
    old_email = USERS[id]['email']
    return render_template('form_update_user.html', users=USERS, id=id, old_name=old_name, old_email=old_email)

@user_route.route('/<int:id>/update', methods=['POST'])
def update_user(id):
    global USERS
    USERS[id]['name'] = request.form['name']
    USERS[id]['email'] = request.form['email']
    return list_users()
