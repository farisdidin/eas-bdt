# app/home

from flask import render_template, jsonify, json, redirect, url_for, request
from flask_login import login_required, current_user

from .. import mongo
from . import home

@home.route('/')
def homepage():
    # return render_template('home/index.html', title="welcome")
    return redirect(url_for('auth.login'))

@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/profile')
@login_required
def profile():
    profil = mongo.db.profil
    user = profil.find_one({'Username': current_user.username},{'_id':False})
    
    return render_template('home/profile.html', title='Profil', profil=user )

@home.route('/profileEdit')
@login_required
def edit():
    profil = mongo.db.profil
    user = profil.find_one({'Username': current_user.username},{'_id':False})

    return render_template('home/profileEdit.html', profil=user)

@home.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    if request.method == 'POST':
        # makan = jsonify(request.form)
        # return makan

        food=request.form.get('foods_new')
        drink=request.form.get('drinks_new')
        hobby=request.form.get('hobbies_new')

        profil = mongo.db.profil
        user = profil.find_one({'Username': current_user.username})
        
        if food:
            profil.update_one({'Username': current_user.username},{'$push':{'Foods':food}})
        if drink:
            profil.update_one({'Username': current_user.username},{'$push':{'Drinks':drink}})
        if hobby:
            profil.update_one({'Username': current_user.username},{'$push':{'Hobbies':hobby}})

        return redirect(url_for('home.profile'))

        
@home.route('/delete/<x>/<y>', methods=['GET'])
@login_required
def delete(x,y):
        profil = mongo.db.profil
        user = profil.find_one({'Username': current_user.username})
        profil.update_one({'Username': current_user.username},{'$pull':{x:y}})
        
        # return render_template('home/profile.html', title='Profil', profil=user )
        return redirect(url_for('home.profile'))
        # return x+y        

# @home.route('/addmongo')
# def add():
#     user = mongo.db.profil
#     user.insert({'name' : 'Didin2', 'food' : ["nasi goreng", "mi ayam"]})
#     return 'Data Added'

# @home.route('/findmongo')
# def find():
#     profil=mongo.db.profil
#     didin = profil.find_one({'name' : 'Didin2'})
#     return 'User '+didin['name']+' suka makan '+didin['food'][0]+' dan '+didin['food'][1]