from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# with app_context():
# db.create_all()

class User(db.Model):
    """"User model """
    __tablename__ = "users"
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    
# with app.app_context():
    # db.create_all()


