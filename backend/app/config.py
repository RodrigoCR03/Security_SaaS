import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/ssdi_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Outras configurações, como API keys, endpoints, etc.
