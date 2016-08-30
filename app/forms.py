from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	"""docstring for ClassName"""
	name = StringField('Your name please', validators=[Required()])
	submit = SubmitField('Submit')