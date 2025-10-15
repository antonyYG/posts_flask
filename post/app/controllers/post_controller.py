from flask import Flask,render_template,redirect,url_for,flash,session,request
from app.models.post_model import Post
from app.app import db

def register_routes(app):

    @app.route('/posts')
    def list_posts():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        posts= Post.query.all()
        return render_template('posts.html' ,posts=posts,username=session['user_name'])
    
    @app.route('/posts/new', methods=['GET', 'POST'])
    def new_post():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            user_id = session['user_id']

            post = Post(title=title, content=content, user_id=user_id)
            db.session.add(post)
            db.session.commit()
            flash('Post creado correctamente', 'success')
            return redirect(url_for('list_posts'))

        return render_template('new_post.html')