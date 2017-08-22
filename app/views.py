from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Thomas'}
	start = 1
	end = 3
	posts = [ #fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers move was so cool!'
		},
		{
			'author': {'nickname': 'Mark'},
			'body': 'The cooking class featured a selection of red chilis.'
		},
		{
			'author': {'nickname': 'River'},
			'body': 'My friend and I had a good time designing the new Bratz doll.'
		}	
	]
	
	posts_slice = posts[start:end]

	return render_template('index.html',  
							user=user,
							posts_slice=posts_slice)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm() #form object is loaded for each request
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
							title='Log In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

