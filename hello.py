from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from app import forms
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET KEY'] = 'rastafari'
bootstrap = Bootstrap(app)
manager = Manager(app)
"""
<=======================================================>
Database configuration
<=======================================================>"""
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
"""
<========================================================>
sessions and redirects
<========================================================>"""
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('looks like you have changed your name')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
		return render_template('index.html', form = form, name = session.get('name')) 
"""
<========================================================>
database in views
<========================================================>"""
@app.route('/' methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user=User(username=form.data.name)
			db.session.add(user)
			session['known']= False 
		else:
			session['known']= True 
			session['name']= form.name.data 
			form.name.data=''
		return(redirect url_for('index'))
	return render_template('insex.html', form = 'form', name = session_get('name'), known = session_get('known', False))

"""
<========================================================>
models 
<========================================================>"""
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	
	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	
	def __repr__(self):
		return '<User %r>' % self.username



