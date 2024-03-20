import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KRY') or '2291277'