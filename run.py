# this file is written because app.py in not run with python3.5 app.py since only the app is taken and we cannot simply
# copy and past "from db import db" because of circular import issues

from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()