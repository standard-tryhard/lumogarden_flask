#!../runner/bin/python
from app import db

class Pool(db.Model):
	__tablename__ = 'pool'
	id = db.Column(db.Integer, primary_key = True)
	pool_name = db.Column(db.String(64), index=True, unique=True)
	pool_items = db.relationship('PoolItems', backref='name', lazy='dynamic')
	
	def __repr__(self):
		return '<Pool %r>' % (self.pool_name)

class PoolItems(db.Model):
	__tablename__ = 'pool_items'
	id = db.Column(db.Integer, primary_key = True)
	task = db.Column(db.String(140))
	category = db.Column(db.Integer, db.ForeignKey('pool.id'))

	def __repr__(self):
		return '<Task %r>' % (self.task)


# class Grid(db.Model):
# 	__tablename__ = 'grid'
# 	id = db.Column(db.Integer, primary_key = True)
# 	grid_name = db.Column(db.String(64), index=True, unique=True)
# 	jars = db.relationship('Jar', backref='name', lazy='dynamic')
	
# 	def __repr__(self):
# 		return '<Grid %r>' % (self.grid_name)


# class Jar(db.Model):
# 	__tablename__ = 'jar'
# 	id = db.Column(db.Integer, primary_key=True)
# 	jar_name = db.Column(db.String(60))
# 	available = db.Column(db.Boolean())
# 	active = db.Column(db.Boolean())
# 	card = db.relationship('CardItems', backref='name', lazy='dynamic')

# 	def __repr__(self):
# 		return '<Jar %r>' % (self.jar_name)


class CardItems(db.Model):
	__tablename__ = 'card_items'
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(140))
	jar = db.Column(db.Integer, db.ForeignKey('jar.id'))

	def __repr__(self):
		return '<CardItems %r>' % (self.card_items)


