from flask import Flask, render_template
from wtform_fields import *
from flask_socketio import SocketIO, send,emit
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URL']= 'postgresql://postgres:postgres@localhost/rchat'
app.debug = True
# db = SQLAlchemy(app)

app.secret_key = 'replace later'

# app.config['SQLALCHEMY_DATABASE_URL']='postgres:'

socketio = SocketIO(app)

@app.route("/", methods=['GET','POST'])
def index():
  
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
     return "Great success!"
   
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

  
if __name__ == '__main__':
    
 socketio.run(app,debug=True)