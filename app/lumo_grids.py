#!../runner/bin/python
import sys
sys.path.append('/Users/thomasoflight/Dropbox/LUMOGRIDS_APP/APP_FLASK')

from app import app, db, models

pools = db.session.query(models.Pool).all()
pools = [pool.pool_name.upper() for pool in pools]


