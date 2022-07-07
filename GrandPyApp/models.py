from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

"""
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, ):

db.create_all()
"""