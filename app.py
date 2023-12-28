from flask import Flask, render_template,request, url_for
from wtform_fields import *
from models import *
from flask_socketio import SocketIO, send,emit
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:admin@localhost:5432/rchat'
app.debug = True
# db.init_app(app)
db = SQLAlchemy(app)

app.secret_key = 'replace later'

try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print(f"Error creating database tables: {e}")

# app.config['SQLALCHEMY_DATABASE_URL']='postgres:'

socketio = SocketIO(app)

@app.route("/", methods=['GET','POST'])
def index():
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
    username = reg_form.username.data
    password =reg_form.password.data
#  return "Great success!"
    user_object = User.query.filter_by(username=username).first()
    if user_object:
      return "Someone else has taken this username!"
    
    user = User(username=username, password=password) 
    db.session.add(user)
    db.session.commit()
    return "Inserted into DB!"
   
  return render_template("index.html",form=reg_form)

@app.route("/chat", methods=['Get','POST'])
def chat():
  # if not current_user.is_authenticated:
  #   flash('Please login.', 'danger')
  #   return redirect(url_for('login'))
    
  return render_template("chat.html")

@socketio.on('message')
def message(data):
  # print(f"\n\n{data}\n\n")
  send(data)
  # emit('some-event', 'this is a custom event message')

  
# with app_context():
    # db.create_all()

if __name__ == '__main__':
    
 socketio.run(app,debug=True)