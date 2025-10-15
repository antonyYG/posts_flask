from flask import request, render_template, redirect, url_for, session, flash
from app.models.user_model import User
from app.app import db

def register_routes(app):
    @app.route('/register', methods=['GET','POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            if User.query.filter_by(email=email).first():
                flash('El correo ya existe' , 'error')
                return redirect(url_for('register'))
            
            user = User(name=name,email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente','success')
            return redirect(url_for('login'))
        return render_template('register.html')
    
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                session['user_name'] = user.name
                flash('Bienvenido' + user.name, 'success')
                return redirect(url_for('list_posts'))
            flash('Error credenciales incorrectas','error')
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
