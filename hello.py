from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from app import forms 


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		return render_template('index.html', form=form, name=name) 

if __name__ == '__main__':
	app.run(debug=True)
