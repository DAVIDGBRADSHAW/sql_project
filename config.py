import os
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/databases-flask-demo"
SQLALCHEMY_DATABASE_URI = os.getenv('DATAABASE_URL', 'sqlite:///db.sqlite3')