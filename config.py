import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here-12345'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/fund_donation_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads/receipts'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
