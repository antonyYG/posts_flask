from app.app import app
from app.extensions import db
from app.models.user_model import User
from app.models.post_model import Post


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
