from flask import render_template, flash, redirect
from app import app, db, models
from .forms import LoginForm

@app.route('/')
@app.route('/grids/')
def grids():
	user = {'nickname': 'Thomas'}

	pools = db.session.query(models.Pool).all()

	return render_template('grids.html',  
							user=user,
							pools=pools)


@app.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

